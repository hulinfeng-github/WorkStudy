[toc]
## 删除分支
- 强制删除本地分支：git branch -D local_branch_name
- 删除远端分支：git push origin -d origin_branch_name 或者 git push origin :origin_branch_name

## 推送到远端分支
git push origin local_branch_name:origin_branch_name

## 设置远端分支与本地关联
git branch --set-upstream-to=origin/origin_branch_name

## 贮藏
git stash save "test-cmd-stash"

## 拉取远端指定分支
 git checkout -b dev_sync_m3.2_lfq origin/dev_sync_m3.2_lfq 

## git合并本地commit
git rebase -i commitID  
*[//]:其中，-i 的参数是不需要合并的 commit 的 hash 值

## 解决分支冲突
如果你想让”mywork“分支历史看起来像没有经过任何合并一样，也可以用 git rebase，如下所示:
``` shell
$ git checkout mywork
$ git rebase origin
```
在rebase的过程中，也许会出现冲突(conflict)。在这种情况，Git会停止rebase并会让你去解决冲突；在解决完冲突后，用”git add“命令去更新这些内容的索引(index), 然后，你无需执行 git commit,只要执行:
```shell
$ git rebase --continue
```

这样git会继续应用(apply)余下的补丁。
在任何时候，可以用--abort参数来终止rebase的操作，并且”mywork“ 分支会回到rebase开始前的状态。
```shell
$ git rebase --abort
```
## 贮藏
- 贮藏 
    ```git stash save "注释"```
- 查看贮藏具体内容
    ```git stash show -p stash@{3}```

## tag用法
git标签分为两种类型：轻量标签和附注标签。轻量标签是指向提交对象的引用，附注标签则是仓库中的一个独立对象。建议使用附注标签。
1. 创建轻量标签
```git tag v0.1.2-light```
2. 创建附注标签
    ```git tag -a v0.1.2 -m “0.1.2版本”```
创建轻量标签不需要传递参数，直接指定标签名称即可。
创建附注标签时，参数a即annotated的缩写，指定标签类型，后附标签名。参数m指定标签说明，说明信息会保存在标签对象中。

- 切换到标签
与切换分支命令相同，用git checkout [tagname]
查看标签信息
用git show命令可以查看标签的版本信息：
    ```git show v0.1.2```

- 删除标签
误打或需要修改标签时，需要先将标签删除，再打新标签。
    ```git tag -d v0.1.2 # 删除标签```
参数d即delete的缩写，意为删除其后指定的标签。

- 给指定的commit打标签
打标签不必要在head之上，也可在之前的版本上打，这需要你知道某个提交对象的校验和（通过git log获取）。

- 补打标签
    ``` git tag -a v0.1.1 9fbc3d0 ```

- 标签发布
通常的git push不会将标签对象提交到git服务器，我们需要进行显式的操作：
    ```git push origin v0.1.2 # 将v0.1.2标签提交到git服务器```
    ```git push origin –tags # 将本地所有标签一次性提交到git服务器```

- 注意：如果想看之前某个标签状态下的文件，可以这样操作
1. git tag  查看当前分支下的标签
2. git  checkout v0.21  此时会指向打v0.21标签时的代码状态，(但现在处于一个空的分支上)
3. cat  test.txt  查看某个文件

- 显示所有标签
    ```git tag -l```

- 删除标签
    - 删除本地tag
    ```git tag -d tag-name```

    - 删除远程tag
    ```git push origin :refs/tags/tag-name```


