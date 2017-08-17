# TTserver 安装
###### 下载
wget http://fallabs.com/tokyocabinet/tokyocabinet-1.4.48.tar.gz
wget http://fallabs.com/tokyotyrant/tokyotyrant-1.1.41.tar.gz
###### 编译安装 tokyocabinet library
cd tokyocabinet-1.4.48
./configure
make
make install

###### 编译安装tokyotyrant server
cd tokyotyrant-1.1.41
./configure
make
make install

###### ttserver 启动参数
`ttserver [-host name] [-port num] [-thnum num] [-tout num] [-dmn] [-pid path] [-kl] [-log path] [-ld|-le] [-ulog path] [-ulim num] [-uas] [-sid num] [-mhost name] [-mport num] [-rts path] [-rcc] [-skel name] [-mul num] [-ext path] [-extpc name period] [-mask expr] [-unmask expr] [dbname]
`
```
-host name : 指定需要绑定的服务器域名或IP地址，默认绑定这台服务器上的所有IP地址。
-port num : 指定需要绑定的端口号，默认端口号为1978
-thnum num : 指定线程数，默认为8个线程
-tout num : 指定每个会话的超时时间（单位为秒），默认永不超时
-dmn : 以守护进程方式运行
-pid path : 输出进程ID到指定文件（这里指定文件名）
-log path : 输出日志信息到指定文件（这里指定文件名）
-ld : 在日志文件中还记录DEBUG调试信息
-le : 在日志文件中仅记录错误信息
-ulog path : 指定同步日志文件存放路径（这里指定目录名）
-ulim num : 指定每个同步日志文件的大小（例如128m）
-uas : 使用异步IO记录更新日志（使用此项会减少磁盘IO消耗，但是数据会先放在内存中，不会立即写入磁盘，如果重启服务器或ttserver进程被kill掉，将导致部分数据丢失。一般情况下不建议使用）。
-sid num : 指定服务器ID号（当使用主辅模式时，每台ttserver需要不同的ID号）
-mhost name : 指定主辅同步模式下，主服务器的域名或IP地址
-mport num : 指定主辅同步模式下，主服务器的端口号
-rts path : 指定用来存放同步时间戳的文件名
-rcc : 复制的一致性检查。
-skel name : 指定骨骼数据库库的名称，什么意思不太明白
-mul num : 指定多个数据库机制的分区数目
-ext path : 指定脚本语言的扩展文件路径
-extpc name period : 指定函数的名称和周期命令的调用周期
-mask expr : 指定禁止执行的命令
-unmask expr : 指定允许的命令的名称
```

###### 管理ttserver
1. stop or terminate ttserver `kill -s SIGINT pid` `kill -s SIGTERM pid`
2. restart ttserver `kill -s SIGHUP pid`


###### 数据库命名方式
1. \* : 内存hash
2. \+ : 内存B+tree
3.  .tch 后缀 hash database
4.  .tcb 后缀 btree database

