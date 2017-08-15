# Linux 常见问题
1. install old version packages
`dnf --showduplicates list kernel`
2. 使用tmpfs 作缓存，临时文件加速
`mkdir /dev/shm/tmp
chmod 777 /dev/shm/tmp
mount --bind /dev/shm/tmp /tmp
`
3. 限制USB 以只读模式挂载
`echo SUBSYSTEM==\"block\",ATTRS{removable}==\"1\",RUN{program}=\"/sbin/blockdev --setro %N\" > /etc/udev/rules.d/80-readonly-removables.rules
udevadm trigger`
4. 
