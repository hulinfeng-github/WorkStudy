目录
[toc]

## 查询文件行数
``` bash
wc -l `find . -name '*.c'` 
```
## 文件重命名
1. mv 源文件 重命名文件
2. rename 老文件 新文件 需要重命名的老文件
3. 批量修改：rename .txt .log *.txt
注：(rename可以利用通配符经行批量修改)

## 卸载软件
sudo apt remove --auto-remove python3.5

## 新增用户
useradd -m username
passwd username

## 切换用户
1.   切换用户的命令为：su username

## docker 使用
docker run  --rm -it --name 'esp32_hlf'  ubuntu:18.04

ctrl+d退出

docker commit CONTAINER ID  esp32idf:latest   
- 注CONTAINER ID 由新开shell窗口 执行docker ps -a得到

docker run --rm -it --name 'esp32_hlf' --privileged -v $PWD:/test esp32idf:latest
docker run --rm -it --name 'esp32_hlf' --privileged -v ${HOME}/Projects/ESP32/hello_world:/projects/hello esp32idf:latest

alias get_idf='. $HOME/Projects/ESP32/esp-idf/export.sh'

user:hulinfeng
passwd:12345678


## 统计代码行数
find . -name *.c|xargs cat|grep -v ^$|wc -l

## 擦除linux 分区
sf probe
sf erase 0x590000 0x1000

## 关闭内核打印
echo 0 > /proc/sys/kernel/printk

## 反汇编 ELF文件
/home/hulinfeng/.espressif/tools/xtensa-esp32s3-elf/esp-2021r2-patch3-8.4.0/xtensa-esp32s3-elf/bin/xtensa-esp32s3-elf-objdump -d ppsapp.elf > 1.txt


## dmesg
可以看到分区表

## MMU 
在计算机系统中，MMU（内存管理单元）是一个硬件组件，负责管理计算机的内存访问，它将逻辑地址（由CPU生成）转换为物理地址（RAM中的实际位置）。MMU的功能对于现代操作系统来说至关重要，它允许多个程序在同一台计算机上并行执行，同时还提供了内存保护和虚拟内存的实现。

在Linux系统中，MMU的主要作用包括以下几个方面：

1. **虚拟内存**：
   - MMU使得Linux能够将物理内存和磁盘上的存储空间结合起来，从而扩展了可用的内存大小。这被称为虚拟内存。MMU负责将程序的虚拟地址映射到物理地址，使得程序可以访问超出实际物理内存容量的数据。

2. **内存保护**：
   - MMU通过设置访问权限位来保护内存区域，防止程序意外地修改或访问其他程序的内存空间。这有助于确保程序之间的隔离和安全性。

3. **地址空间隔离**：
   - 每个运行的程序都拥有自己的地址空间，使得它们可以在不干扰彼此的情况下并行执行。这使得多任务处理成为可能。

4. **页面管理**：
   - MMU负责将物理内存划分成固定大小的页面，并管理这些页面的分配和回收。Linux使用了分页机制，将内存划分成大小为4KB的页面。

5. **缓存管理**：
   - MMU可以将数据从内存复制到高速缓存中，以提高处理器对数据的访问速度。它还可以确保缓存中的数据与实际内存中的数据保持一致。

6. **TLB（转换后备缓冲器）**：
   - TLB是MMU的一部分，用于缓存虚拟地址到物理地址的映射关系，以提高地址转换的速度。TLB可以减少对内存的频繁访问。

总的来说，MMU在Linux系统中扮演着至关重要的角色，它是实现虚拟内存、多任务处理和内存保护的关键组件。通过MMU，Linux能够高效地管理内存，为多个程序提供独立的地址空间，并提供了一系列的内存保护和访问控制机制，从而保障了系统的稳定性和安全性。

## 文件和目录

|指令|说明|
|-----------------------|:----------------------------:|
|cd /home               |	进入 '/ home' 目录'       |
|cd ..	|返回上一级目录| 
|cd ../..|	返回上两级目录|
|cd	|进入个人的主目录|
|cd ~user1|	进入个人的主目录 |
|cd -|	返回上次所在的目录|
|pwd|	显示工作路径|
|ls	|查看目录中的文件| 
|ls -F	|查看目录中的文件| 
|ls -l|	显示文件和目录的详细资料|
|ls -a	|显示隐藏文件| 
|ls *[0-9]*|	显示包含数字的文件名和目录名|
|tree	|显示文件和目录由根目录开始的树形结构|
|lstree|	显示文件和目录由根目录开始的树形结构|
|mkdir dir1|	创建一个叫做 'dir1' 的目录'|
|mkdir dir1 dir2	|同时创建两个目录|
|mkdir -p /tmp/dir1/dir2	|创建一个目录树 |
|rm -f file1	|删除一个叫做 'file1' 的文件'| 
|rmdir dir1|	删除一个叫做 'dir1' 的目录'|
|rm -rf dir1	|删除一个叫做 'dir1' 的目录并同时删除其内容|
|rm -rf dir1 dir2	|同时删除两个目录及它们的内容 |
|mv dir1 new_dir	|重命名/移动 一个目录 |
|cp file1 file2	|复制一个文件 
|cp dir/* .|	复制一个目录下的所有文件到当前工作目录 |
|cp -a /tmp/dir1 .	|复制一个目录到当前工作目录 |
|cp -a dir1 dir2	|复制一个目录|
|cp -r dir1 dir2|	复制一个目录及子目录|
|ln -s file1 lnk1|创建一个指向文件或目录的软链接|
|ln file1 lnk1	|创建一个指向文件或目录的物理链接|

## 文件搜索

|指令|说明|
|--------------------------|:------------------------:|
|ind / -name file1	|从 '/' 开始进入根文件系统搜索文件和目录|
|find / -user user1	|搜索属于用户 'user1' 的文件和目录|
|find /home/user1 -name \*.bin	|在目录 '/ home/user1' 中搜索带有'.bin' 结尾的文件|
|find /usr/bin -type f -atime +100	|搜索在过去100天内未被使用过的执行文件 |
|find /usr/bin -type f -mtime -10|	搜索在10天内被创建或者修改过的文件|
|find / -name \*.rpm -exec chmod 755 '{}' \;	|搜索以 '.rpm' 结尾的文件并定义其权限|
|find / -xdev -name \*.rpm	|搜索以 '.rpm' 结尾的文件，忽略光驱、捷盘等可移动设备|
|locate \*.ps	|寻找以 '.ps' 结尾的文件 - 先运行 'updatedb' 命令|
|whereis halt	|显示一个二进制文件、源码或man的位置|
|which halt	|显示一个二进制文件或可执行文件的完整路径|

## 查看文件内容

|指令|说明|
|--------------------------|:------------------------:|
|cat file1	|从第一个字节开始正向查看文件的内容
|tac file1	|从最后一行开始反向查看一个文件的内容
|more file1	|查看一个长文件的内容
|less file1|	类似于 'more' 命令，但是它允许在文件中和正向操作一样的反向操作
|head -2 file1|	查看一个文件的前两行 
|tail -2 file1	|查看一个文件的最后两行
|tail -f /var/log/messages|	实时查看被添加到一个文件中的内容|

## 打开和压缩文件

|指令|说明|
|--------------------------|:------------------------:|
|bunzip2 file1.bz2	|解压一个叫做 'file1.bz2'的文件|
|bzip2 file1	|压缩一个叫做 'file1' 的文件 |
|gunzip file1.gz	|解压一个叫做 'file1.gz'的文件 |
|gzip file1|	压缩一个叫做 'file1'的文件|
|gzip -9 file1	|最大程度压缩|
|rar a file1.rar test_file	|创建一个叫做 'file1.rar' 的包|
|rar a file1.rar file1 file2 dir1|	同时压缩 'file1', 'file2' 以及目录 'dir1' |
|rar x file1.rar	|解压rar包 |
|unrar x file1.rar	|解压rar包 |
|tar -cvf archive.tar file1|	创建一个非压缩的 tarball |
|tar -cvf archive.tar file1 file2 dir1	|创建一个包含了 'file1', 'file2' 以及 'dir1'的档案文件|
|tar -tf archive.tar	|显示一个包中的内容|
|tar -xvf archive.tar	|释放一个包 |
|tar -xvf archive.tar -C /tmp	|将压缩包释放到 /tmp目录下|
|tar -cvfj archive.tar.bz2 dir1	|创建一个bzip2格式的压缩包| 
|tar -jxvf archive.tar.bz2	|解压一个bzip2格式的压缩包|
|tar -cvfz archive.tar.gz dir1	|创建一个gzip格式的压缩包|
|tar -zxvf archive.tar.gz	|解压一个gzip格式的压缩包 |
|zip file1.zip file1	|创建一个zip格式的压缩包|
|zip -r file1.zip file1 file2 dir1	|将几个文件和目录同时压缩成一个zip格式的压缩包 |
|unzip file1.zip	|解压一个zip格式压缩包 |

## 系统信息

|指令|说明|
|--------------------------|:------------------------:|
|arch	|显示机器的处理器架构|
|uname -m	|显示机器的处理器架构|
|uname -r	|显示正在使用的内核版本|
|dmidecode -q	|显示硬件系统部件 - (SMBIOS / DMI) |
|hdparm -i /dev/hda	|罗列一个磁盘的架构特性 |
|hdparm -tT /dev/sda	|在磁盘上执行测试性读取操作 |
|cat /proc/cpuinfo	|显示CPU info的信息|
|cat /proc/interrupts|	显示中断|
|cat /proc/meminfo	|校验内存使用|
|cat /proc/swaps|	显示哪些swap被使用|
|cat /proc/version	|显示内核的版本|
|cat /proc/net/dev	|显示网络适配器及统计|
|cat /proc/mounts	|显示已加载的文件系统 |
|lspci -tv	|罗列 PCI 设备|
|lsusb -tv	|显示 USB 设备 |
|date|	显示系统日期|
|cal 2007	|显示2007年的日历表|
|date 041217002007.00|	设置日期和时间 - 月日时分年.秒|
|clock -w	|将时间修改保存到 BIOS |

## 关机

|指令|说明|
|--------------------------|:------------------------:|
|shutdown -h now	|关闭系统|
|init 0	|关闭系统|
|telinit 0	|关闭系统|
|shutdown -h hours:minutes &|	按预定时间关闭系统 |
|shutdown -c	|取消按预定时间关闭系统|
|shutdown -r now	|重启|
|reboot	|重启|
|logout	|注销 |
