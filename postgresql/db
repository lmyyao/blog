
需求介绍
1. 单个奖品获取用户总数
2. 获取用户百分比
3. 获取用户是否中奖


量级
1. 奖品1000
2. 用户十万级别 模拟用1万
3. 尝试次数平均10次 大概100万级别
4. 如果但表的话 1000 * 100 万 10亿条


设计
1. 根据奖品ID分表
2. 可以多次抽奖所以userid 对应score 是一对多
3. 可以设计成userid 对应array， 也可以设计成一对多

用例1
表结构
    create table test（userid varchar(255), score int）; //辅助字段略
    create index on test (userid) // btree index
    create index on test (score); // btree index

测试数据 1.py

```
获取中奖用户
select * from test where score = <>
使用score index 20ms
```

```
获取抽奖总数
select count(*) from (select userid from test group by userid) s;
使用userid index 60ms，在这个例子中有很多的重复， 对于更大的数量极可能不是一个很好的选择可以brin index
```

```
获取用户百分比
select count(*) from (select count(userid) from test group by userid having count(userid) > (select count(*) from test where userid = 'user4455')) s;

这里使用到userID index 65ms,
```


用例2 2.py

表结构
    create table test1（userid varchar(255), score int[]）; //辅助字段略
    create index on test1 (userid);
    create index on test1 (array_length(score, 1)) //;
    create index on test1 using gin(score);
测试数据 2.py
由于单表数量比上面的用例小10 倍左右

```
select * from test1 where '{score}'::int[] <@ score;
使用gin 索引, 查询比用例一快15倍 1.2ms
```

```
select count(*) from test1;
使用userid index 5.5ms 快用例一10 倍
```

```
select count(*) from test1 where array_length(score, 1)  > (select array_length(score, 1) from test1 where userid = 'user445')
使用array_length, userid 索引 5.7ms 快10倍
```

比较
1. 查询性能 用例2 大约快1 10倍
2. 扩展 1 的扩展性更好， 比如每天限制用户抽奖几次
3. 插入性能，用例1 更好
