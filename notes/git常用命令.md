1. 初始化本地git仓库（创建新仓库）

   ```shell
   git init
   ```

2. 配置用户名 

   ```shell
   git config --global user.name "xxx" 
   ```

3. 配置邮件 

   ```shell
   git config --global user.email "xxx@xxx.com"
   ```

4. clone远程仓库 

   ```shell
   git clone git+ssh://git@192.168.53.168/VT.git
   ```

   

5. 查看当前版本状态（是否修改） 

   ```shell
   git status
   ```

   

6. 添加xyz文件至

   ```shell
   index git add xyz
   ```

   

7. 增加当前子目录下所有更改过的文件至

   ```shell
   index git add .
   ```

   

8. 提交 

   ```shell
   git commit -m 'xxx' 
   ```

   

9. 合并上一次提交（用于反复修改）

   ```shell
   git commit --amend -m 'xxx' 
   ```

   

10. 将add和commit合为一步 

    ```shell
    git commit -am 'xxx' 
    ```

    

11. 删除index中的文件 

    ```shell
    git rm xxx 
    ```

    

12. 递归删除  

    ```shell
    git rm -r * 
    ```

    

13. 显示提交日志  

    ```shell
    git log
    ```

    

14. 显示1行日志 -n为n行  

    ```shell
    git log -1
    ```

    

15. 显示提交日志及相关变动文件 

    ```shell
    git log --stat 
    ```

    

16. 显示某个提交的详细内容 

    ```shell
    git show dfb02e6e4f2f7b573337763e5c0013802e392818
    ```

    

17. 显示HEAD提交日志  

    ```shell
    git show HEAD
    ```

    

18. 显示所有未添加至index的变更 

    ```shell
    git diff
    ```

    

19. 显示所有已添加index但还未commit的变更 

    ```shell
    git diff --cached 
    ```

    

20. 比较远程分支master上有本地分支master上没有的  

    ```shell
    git diff origin/master..master 
    ```

    

21. 只显示差异的文件，不显示具体内容 

    ```shell
    git diff origin/master..master --stat 
    ```

    

22. 增加远程定义（用于push/pull/fetch） 

    ```shell
    git remote add origin git+ssh://git@192.168.53.168/VT.git
    ```

    

23. 显示本地分支  

    ```shell
    git branch 
    ```

    

24. 显示包含提交50089的分支 

    ```shell
    git branch --contains 50089
    ```

    

25. 显示所有分支 

    ```shell
    git branch -a 
    ```

    

26. 显示所有已合并到当前分支的分支 

    ```shell
    git branch --merged 
    ```

    

27. 显示所有未合并到当前分支的分支  

    ```shell
    git branch --no-merged 
    ```

    

28. 本地分支改名 

    ```shell
    git branch -m master master_copy 
    ```

    

29. 从当前分支创建新分支master_copy并检出 

    ```shell
    git checkout -b master_copy 
    ```

    

30. 合并远程master分支至当前分支 

    ```shell
    git merge origin/master 
    ```

    

31. 合并提交ff44785404a8e的修改 

    ```shell
    git cherry-pick ff44785404a8e 
    ```

    

32. 将当前分支push到远程master分支 

    ```shell
    git push origin master  
    ```

    

33. 删除远程仓库的hotfixes/BJVEP933分支    

    ```shell
    git push origin :hotfixes/BJVEP933
    ```

    

34. 获取所有远程分支（不更新本地分支，另需merge）  

    ```shell
    git fetch 
    ```

    

35. 获取所有原创分支并清除服务器上已删掉的分支   

    ```shell
    git fetch --prune
    ```

    

36. 获取远程分支master并merge到当前分支 

    ```shell
    git pull origin master 
    ```

    

37. 重命名文件README为README2  

    ```shell
    git mv README README2
    ```

    

38. 将当前版本重置为HEAD（通常用于merge失败回退） 

    ```shell
    git reset --hard HEAD 
    ```

    

39. 删除分支hotfixes/BJVEP933（本分支修改已合并到其他分支） 

    ```shell
    git branch -d hotfixes/BJVEP933
    ```

    

40. 强制删除分支hotfixes/BJVEP933 

    ```shell
    git branch -D hotfixes/BJVEP933
    ```

    

41. 撤销提交dfb02e6e4f2f7b5 

    ```shell
    git revert dfb02e6e4f2f7b5
    ```

42. 强制拉取远程仓库代码覆盖本地

    ```shell
    git fetch --all && git reset --hard origin/master && git pull
    ```

    
