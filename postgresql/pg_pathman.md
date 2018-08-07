# pg_pathman
### 安装
1. git clone https://github.com/postgrespro/pg_pathman
2. cd pg_pathman
3. make USE_PGXS=1
4. make USE_PGXS=1 install
5. vi postgresql.conf
	shared_preload_libraries = 'pg_pathman,pg_stat_statements' 
6. pg_ctl restart -m fast
7. psql 
	postgres=# create extension pg_pathman;

### 分区
> 创建分区表时，需要指定主表的名字，主表必须已存在，主表可以有数据，也可以是空表
> 如果主表有数据，那么可以配置是否需要在创建分区时，将数据迁移到分区，（不建议对大表这么做）
> 如果主表有很多数据，建议使用后台非堵塞式的迁移方法（调用partition_table_concurrently()函数进行迁移)
> 目前支持两种分区，range分区个hash分区

###### range 分区
指定起始值、间隔、分区个数
```
create_range_partitions ( 
						relation       REGCLASS,  -- 主表OID
                        attribute      TEXT,      -- 分区列名
                        start_value    ANYELEMENT,  -- 开始值
                        p_interval     ANYELEMENT,  -- 间隔；任意类型，适合任意类型的分区表
                        p_count        INTEGER DEFAULT NULL,   --  分多少个区
                        partition_data BOOLEAN DEFAULT TRUE)   --  是否立即将数据从主表迁移到分区, 
-- 不建议这么使用, 建议使用非堵塞式的迁移( 调用partition_table_concurrently()
```
指定起始值、终值、间隔
```
create_partitions_from_range (
							relation       REGCLASS,  -- 主表OID
                             attribute      TEXT,      -- 分区列名
                             start_value    ANYELEMENT,  -- 开始值
                             end_value      ANYELEMENT,  -- 结束值
                             p_interval     ANYELEMENT,  -- 间隔；任意类型，适合任意类型的分区表
                             partition_data BOOLEAN DEFAULT TRUE)   --  是否立即将数据从主表迁移到分区, 不建议这么使用, 建议使用非堵塞式的迁移( 调用partition_table_concurrently() )
```
建议
1. 分区列必须有not null约束
2. 分区个数必须能覆盖已有的所有记录
3. 建议使用非堵塞式迁移接口
4. 建议数据迁移完成后，禁用主表
###### hash 分区
指定起始值、间隔、分区个数
```
create_hash_partitions(relation         REGCLASS,  -- 主表OID
                       attribute        TEXT,      -- 分区列名
                       partitions_count INTEGER,   -- 打算创建多少个分区
                       partition_data   BOOLEAN DEFAULT TRUE)   --  是否立即将数据从主表迁移到分区, 不建议这么使用, 建议使用非堵塞式的迁移( 调用partition_table_concurrently() )
```
建议
1. 分区列必须有not null约束
2. 建议使用非堵塞式迁移接口
3. 建议数据迁移完成后，禁用主表
4. pg_pathman不会受制于表达式的写法，所以select * from part_test where crt_time = '2016-10-25 00:00:00'::timestamp;这样的写法也是能走哈希分区的。
5. hash分区列不局限于int类型的列，会使用hash函数自动转换

例子:
```
#创建分区主表
Test=# create table part_test(id int, info text, crt_time timestamp not null);
CREATE TABLE
Test=# insert into part_test select id,md5(random()::text),clock_timestamp() from generate_series(1,10000) t(id);
INSERT 0 10000
Test=# select * from part_test limit 10;
 id |               info               |          crt_time          
----+----------------------------------+----------------------------
  1 | ab8e5ee0448a2b4ad61d7e0e767ee1ea | 2016-11-02 16:04:18.294478
  2 | 28a626af632e0ccebbd111a3e1a240e1 | 2016-11-02 16:04:18.294745
  3 | faf2f529a9a83d27b6e13e68ee8e7407 | 2016-11-02 16:04:18.294761
  4 | f4afc8263ea625000305825efff52eaa | 2016-11-02 16:04:18.294768
  5 | 385d942fded21a969f5c0dda64cb1aad | 2016-11-02 16:04:18.294774
  6 | 703f3bee94e322e3234a50cfed01ad24 | 2016-11-02 16:04:18.29478
  7 | 6e28eac2c127263860929b4c24b46a09 | 2016-11-02 16:04:18.294787
  8 | 68b9e8133af0aa1b024aa323ffae0c9c | 2016-11-02 16:04:18.294793
  9 | 58428fa313fc49d13dc14dad18b10fad | 2016-11-02 16:04:18.294799
 10 | cd2cb16088f7304a1f08cd9c9b774fd9 | 2016-11-02 16:04:18.294805
(10 rows)

Test=# select create_range_partitions(
'part_test'::regclass, --主表oid
'crt_time',  --分区字段，一定要not null约束
'2016-11-02 00:00:00'::timestamp, --开始时间
interval '1 month',   --分区间隔，一个月
10,  --分区表数量
false  --  不立即将数据从主表迁移到分区,
);

# partition_table_concurrently(relation   REGCLASS,              -- 主表OID
                             batch_size INTEGER DEFAULT 1000,  -- 一个事务批量迁移多少记录
                             sleep_time FLOAT8 DEFAULT 1.0)    -- 获得行锁失败时，休眠多久再次获取，重试60次退
                            
Test=# select partition_table_concurrently('part_test'::regclass,10000,1.0);
Test=# select count(*) from only part_test;
 count 
-------
     0
# 数据迁移完成后，建议禁用主表，这样执行计划就不会出现主表了
Test=# select set_enable_parent('part_test'::regclass, false);
 set_enable_parent 
-------------------

(1 row)
```

### 分区管理
相关视图和表
1. pathman_config
2. pathman_config_params
3. pathman_concurrent_part_tasks
4.  pathman_partition_list
5.  pathman_cache_stats 

查看后台的数据迁移任务
`select * from pathman_concurrent_part_tasks`

如何停止迁移任务
`select stop_concurrent_part_task(relation REGCLASS)`
                  

Refer:

[https://yq.aliyun.com/articles/62314](https://yq.aliyun.com/articles/62314#)

[https://github.com/postgrespro/pg_pathman](https://github.com/postgrespro/pg_pathman)
