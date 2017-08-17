# Linux 常见问题
1. install old version packages
`dnf --showduplicates list kernel`
2. 使用tmpfs 作缓存，临时文件加速
`mkdir /dev/shm/tmp
chmod 777 /dev/shm/tmp
mount --bind /dev/shm/tmp /tmp
`
3.  限制USB 以只读模式挂载
`echo SUBSYSTEM==\"block\",ATTRS{removable}==\"1\",RUN{program}=\"/sbin/blockdev --setro %N\" > /etc/udev/rules.d/80-readonly-removables.rules
udevadm trigger`
4. 编译软件常常会出现configure:  error:  *****.h is required
`1. 确认系统是否有这个*.h执行命令 locate *.h`
`2. 如果没有找到*.h 那么需要下载包含*.h 的软件包`
`3. 如果找到*.h C_INCLUDE_PATH=<查找到的路径> ./configure`
5.  编译软件make常常会出现:  *****.so not found
`1. 确认系统是否有这个*.so执行命令 locate *.so`
`2. 如果没有找到*.so 那么需要下载包含*.so 的软件包`
`3. 如果找到*.so LD_LIBRARY_PATH=<查找到的路径> make`

6. 编译软件使用clang 编译器
`1. make CC=clang (对于c程序)`
`2. make CXX=clang++ （c++程序）`
