###编写Telegraf Input 插件

Telegraf是一个Influxdata的数据采集套件，使用起来跟Collectd、Statsd、Logstash等软件很像。通过plugin来实现数据的input和output。 今天我们尝试自己编写一个采集supervisord的插件

1. 准备golang （最好1.9+）环境， 
2. 准备一些dep 编译环境 https://golang.github.io/dep/docs/installation.html
3. 准备http_proxy （你懂的）
4. go get github.com/influxdata/telegraf
5. cd $GOPATH/github.com/influxdata/telegraf
6. git checkout -b supervisor
7. cd plugins/inputs
8. mkdir supervisor
9.  cd supervisor
10. 参考https://github.com/influxdata/telegraf/blob/master/CONTRIBUTING.md#input-plugin-example 
11. vim telegraf/plugins/inputs/all/all.go
    追加一行
    _ "github.com/influxdata/telegraf/plugins/inputs/supervisor"
12. cd $GOPATH/github.com/influxdata/telegraf
13. make
14. ./telegraf  --help

15 ./telegraf --input-filter supervisor config > telegraf.conf

16 ./telegraf --config telegraf.conf --test


