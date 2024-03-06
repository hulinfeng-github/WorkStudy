**目录**
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [简介](#简介)
- [相关文章](#相关文章)
- [目录](#目录)
- [引用](#引用)
- [分割线](#分割线)
- [超链接](#超链接)
- [强调](#强调)
- [删除线](#删除线)
- [注释](#注释)
- [表格](#表格)
- [task list](#task-list)
- [图像](#图像)
  - [标准流程图](#标准流程图)
  - [标准流程图横向](#标准流程图横向)
  - [UML 时序流程图](#uml-时序流程图)
  - [甘特图](#甘特图)
- [导入外部文件](#导入外部文件)
- [官方教程文档](#官方教程文档)

<!-- /code_chunk_output -->

## 简介
- 使用vscode中的插件：`Markdown Preview Enhanced`的预览功能

## 相关文章
1. <https://www.bookstack.cn/read/mpe/zh-cn-markdown-basics.md>

## 目录
- 可以通过 cmd-shift-p 然后选择 `Markdown Preview Enhanced: Create Toc `命令来创建 TOC。多个 TOCs 可以被创建。如果你想要在你的 TOC 中排除一个标题，请在你的标题 后面 添加 {ignore=true} 即可。

## 引用
>引用内容  
>应用内容  
>> 引用内容  

## 分割线

***
---
___

* * *
- - -

## 超链接

- [文本](link)
- 自动链接:<https://www.baidu.com/>

![GitHub](https://avatars2.githubusercontent.com/u/3265208?v=3&s=100 "GitHub,Social Coding")

## 强调
- 这是用来 *演示* 的 _文本_
这是用来 **演示** 的 __文本__

## 删除线
这就是 ~~删除线~~

## 注释
[//]: 注释
[^_^]: (注释不会显示)

## 表格
| left | center | right |
| :--- | :----: | ----: |
| aaaa | bbbbbb | ccccc |
| a    | b      | c     |

## task list
- [ ] Eat
- [x] Code
  - [x] HTML
  - [x] CSS
  - [x] JavaScript
- [ ] Sleep

## 图像

```sequence {theme="hand"}
Andrew->China:Says Hello
Note right of China:China thinks\nabout it
China-->Andrew:How are you?
Andrew->>China:I am good thanks!
```

```mermaid
graph LR
A-->B;
B-->C;
C-->A;
```
### 标准流程图

```flow
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框
st->op->cond
cond(yes)->io->e
cond(no)->sub1(right)->op
```

### 标准流程图横向

```flow
st=>start: 开始框
op=>operation: 处理框
cond=>condition: 判断框(是或否?)
sub1=>subroutine: 子流程
io=>inputoutput: 输入输出框
e=>end: 结束框
st(right)->op(right)->cond
cond(yes)->io(bottom)->e
cond(no)->sub1(right)->op
```

### UML 时序流程图 
```sequence
Title: 标题：复杂使用
对象A->对象B: 对象B你好吗?（请求）
Note right of 对象B: 对象B的描述
Note left of 对象A: 对象A的描述(提示)
对象B-->对象A: 我很好(响应)
对象B->小Q: 你好吗
小Q-->>对象A: 对象B找我了
对象A->对象B: 你真的好吗？
Note over 小Q,对象B: 我们是朋友
participant C
Note right of C: 没人陪我玩
```
```mermaid
%% 时序图例子,-> 直线，-->虚线，->>实线箭头
  sequenceDiagram
    participant 张三
    participant 李四
    张三->王五: 王五你好吗？
    loop 健康检查
        王五->王五: 与疾病战斗
    end
    Note right of 王五: 合理 食物 <br/>看医生...
    李四-->>张三: 很好!
    王五->李四: 你怎么样?
    李四-->王五: 很好!
```

### 甘特图
```mermaid
%% 语法示例
        gantt
        dateFormat  YYYY-MM-DD
        title 软件开发甘特图
        section 设计
        需求                      :done,    des1, 2014-01-06,2014-01-08
        原型                      :active,  des2, 2014-01-09, 3d
        UI设计                     :         des3, after des2, 5d
    未来任务                     :         des4, after des3, 5d
        section 开发
        学习准备理解需求                      :crit, done, 2014-01-06,24h
        设计框架                             :crit, done, after des2, 2d
        开发                                 :crit, active, 3d
        未来任务                              :crit, 5d
        耍                                   :2d
        section 测试
        功能测试                              :active, a1, after des3, 3d
        压力测试                               :after a1  , 20h
        测试报告                               : 48h
```

## 导入外部文件
`@import "你的文件"`

## 官方教程文档
- [官方文档](https://markdown.com.cn/basic-syntax/)

