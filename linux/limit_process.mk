#### Limit Program Memory By Cgroup
1. cgcreate -g memory:/myGroup
2. echo $(( 500 * 1024 * 1024 )) > /sys/fs/cgroup/memory/myGroup/memory.limit_in_bytes(`notes`: centos cgroup mount on /sys/fs/cgroup)
3. echo '@\<username\>:\<command\> memory /myGroup' >> /etc/cgrules.conf
4. systemctl restart cgred
5. cgget -g memory /myGroup (查看/myGroup的配置,以及内存使用情况)
6. cat /proc/\<pid\>/cgroup

