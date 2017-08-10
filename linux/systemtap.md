# SystemTap 常用命令
1. `man probe::*  man function::* man tapset::*`
2. `stap -L 'kernel.function("*")'`  `stap -L 'kernel.function("vfs_*")'`
3. `stap -e 'probe kernel.function("vfs_read") {printf("%s\n", $$parms$); exit(); }'` `stap -e 'probe kernel.function("vfs_read") {printf("%s\n", $$parms$$); exit(); }'`
