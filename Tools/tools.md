**好用的工具可以大大提高生产力**

**目录**
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [好用的工具](#好用的工具)
- [好用的vscode插件](#好用的vscode插件)
- [wireshark使用技巧](#wireshark使用技巧)
  - [过滤规则](#过滤规则)
- [stackoverflow搜索技巧](#stackoverflow搜索技巧)

<!-- /code_chunk_output -->

## 好用的工具 
- 截图工具:snipaste
- 窗口管理工具:Q-Dir
- 搜索工具:uTools，everything
- 抓包分析工具:omnipeek,wireshark
- 视频播放工具：vlc
- 比较工具：WinMerge, beyond compare
- 手机投屏工具：QtScrcpy
- 串口工具：sscom,crt
- 远程连接工具：crt
- 编辑器:notepad++
- http调试工具:postman

## 好用的vscode插件
- 括号区分：Bracket Pair Color DLW
- Git :GIT Graph
- 主题：GitHub Theme
- markdown: Markdown Preview Enhanced, Markdown Preview Mermaid Support, Markmap

## wireshark使用技巧
### 过滤规则
- 协议过滤
    - TCP：只显示TCP协议的数据流
    - HTTP：只显示HTTP协议的数据流
    - ICMP：只显示ICMP协议的数据流
    - ARP：只显示ARP协议的数据流
    - DNS：显示DNS协议的数据流

- IP过滤
    - ip.addr = 192.168.0.123，只显示ip为192.168.0.123有关的数据流
    - ip.src = 192.168.0.123，只显示源IP地址为192.168.0.123的数据流
    - ip.dst = 192.168.0.123，只显示目标IP地址为192.168.0.123的数

- 端口过滤
    - tcp.port == 80，只显示80端口TCP数据流
    - udp.prot == 67，只显示67端口UDP数据流
    - tcp.srcport == 80, 只显示源地址的80端口数据流
    - tcp.dstport == 80，只显示目的地址80端口数据流

- 过滤HTTP协议
    - http.request.method==“GET”，显示get请求
    - http.request.method==“POST” ，显示POST请求
    - http.request.url contains admin ，显示url中包含admin的请求
    - http.request.code==404，显示状态码为404
    - http contains “FLAG”，请求或相应中包含特定内容

- 包长过滤
    - udp.length==20，整个UDP数据包
    - tcp.len>=20，TCP数据包中的IP数据包
    - ip.len==20，整个IP数据包
    - frame.len==20，整个数据包

- 常用过滤条件
    wlan.addr == 10:91:a8:a9:58:d4 || (wlan.addr == d4:bd:4f:13:02:f8 && (wlan.fc == 0x8000 || wlan.fc == 0xd400 || wlan.addr == ff:ff:ff:ff:ff:ff)) 

    (((wlan.sa == b0:df:c1:0f:12:11) && (wlan.da == ff:ff:ff:ff:ff:ff)) || ((wlan.sa == 40:4c:ca:41:00:80)) && (wlan.da == b0:df:c1:0f:12:11))

    wlan.addr == 40:4c:ca:41:00:80 || (wlan.addr == b0:df:c1:0f:12:11 && (wlan.fc == 0x8000 || wlan.fc == 0xd400 || wlan.addr == ff:ff:ff:ff:ff:ff)) 
## stackoverflow搜索技巧
- [stackoverflow搜索](https://blog.csdn.net/weixin_44671418/article/details/107515048)

