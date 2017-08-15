# Linux Parallel 使用
你是否曾经有过要计算一个非常大的数据(几百GB)的需求？或在里面搜索，或其它操作——一些无法并行的操作。数据专家们，我是在对你们说。你可能有一个4核或更多核的CPU，但我们合适的工具，例如 grep, bzip2, wc, awk, sed等等，都是单线程的，只能使用一个CPU。

要想让Linux命令使用所有的CPU，我们需要用到GNU Parallel命令，它让我们所有的CPU内核在单机内做神奇的map-reduce操作，当然，这还要借助很少用到的–pipes 参数(也叫做–spreadstdin)。这样，你的负载就会平均分配到各CPU上，真的

例子：

1. `cat bigfile.txt | parallel --pipe -k bzip --best > comp.bz`
2. `cat bigfile.txt | parallel --block 10M --pipe grep 'pattern'`
3. `cat bigfile.txt | parallel  --pipe wc -l | awk '{s+=$1} END {print s}'`
4. `cat bigfile.txt | parallel --pipe sed s^old^new^g`
5. `seq 0 100|parallel -N 10 'echo {} {#}'`
6. `parallel echo  ::: $(seq 30) ::: $(seq -w 24)` 

```
Download 24 images for each of the past 30 days

Let us assume a website stores images like:

http://www.example.com/path/to/YYYYMMDD_##.jpg
where YYYYMMDD is the date and ## is the number 01-24. This will download images for the past 30 days:

getit() {
    date=$(date -d "today -$1 days" +%Y%m%d)
    num=$2
    echo wget http://www.example.com/path/to/${date}_${num}.jpg
}
export -f getit

parallel getit ::: $(seq 30) ::: $(seq -w 24)
$(date -d "today -$1 days" +%Y%m%d) will give the dates in YYYYMMDD with $1 days subtracted.
```

[Man 帮助](https://www.gnu.org/software/parallel/man.html#EXAMPLE:-Reading-arguments-from-command-line)
