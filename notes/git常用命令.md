1. 初始化本地git仓库（创建新仓库）

   ```shell
   git init
   ```

2. 配置用户名 git config --global user.name "xxx" 

3. 配置邮件 git config --global user.email "xxx@xxx.com"

4. clone远程仓库 git clone git+ssh://git@192.168.53.168/VT.git

5. 查看当前版本状态（是否修改）git status 

6. 添加xyz文件至index git add xyz

7. 增加当前子目录下所有更改过的文件至index git add .

8. 提交 git commit -m 'xxx' 

9. 合并上一次提交（用于反复修改）git commit --amend -m 'xxx' 

10. 将add和commit合为一步 git commit -am 'xxx' 

11. 删除index中的文件 git rm xxx 

12. 递归删除  git rm -r * 

13. 显示提交日志 git log 

14. 显示1行日志 -n为n行  git log -1

15. 显示提交日志及相关变动文件 git log --stat 

16. 显示某个提交的详细内容 git show dfb02e6e4f2f7b573337763e5c0013802e392818

17. 显示HEAD提交日志  git show HEAD

18. 显示所有未添加至index的变更 git diff

19. 显示所有已添加index但还未commit的变更 git diff --cached 

20. 比较远程分支master上有本地分支master上没有的  git diff origin/master..master 

21. 只显示差异的文件，不显示具体内容 git diff origin/master..master --stat 

22. 增加远程定义（用于push/pull/fetch） git remote add origin git+ssh://git@192.168.53.168/VT.git

23. 显示本地分支  git branch 

24. 显示包含提交50089的分支 git branch --contains 50089

25. 显示所有分支 git branch -a 

26. 显示所有已合并到当前分支的分支 git branch --merged 

27. 显示所有未合并到当前分支的分支  git branch --no-merged 

28. 本地分支改名 git branch -m master master_copy 

29. 从当前分支创建新分支master_copy并检出 git checkout -b master_copy 

30. 合并远程master分支至当前分支 git merge origin/master 

31. 合并提交ff44785404a8e的修改 git cherry-pick ff44785404a8e 

32. 将当前分支push到远程master分支 git push origin master  

33. 删除远程仓库的hotfixes/BJVEP933分支  git push origin :hotfixes/BJVEP933  

34. 获取所有远程分支（不更新本地分支，另需merge）  git fetch 

35. 获取所有原创分支并清除服务器上已删掉的分支  git fetch --prune 

36. 获取远程分支master并merge到当前分支 git pull origin master 

37. 重命名文件README为README2 git mv README README2 

38. 将当前版本重置为HEAD（通常用于merge失败回退） git reset --hard HEAD 

39. 删除分支hotfixes/BJVEP933（本分支修改已合并到其他分支） git branch -d hotfixes/BJVEP933

40. 强制删除分支hotfixes/BJVEP933 git branch -D hotfixes/BJVEP933

41. 撤销提交dfb02e6e4f2f7b5 git revert dfb02e6e4f2f7b5

