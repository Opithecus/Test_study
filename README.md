# Test_study
欲速则不达。

测试从GitHub端pull到本地。更新数据。



1.推送本地文件到Github

进入本地项目目录，右键点击Git Bash Here

```
git add .   //添加当前目录下的所有文件到暂存区
git commit -m "init project"   //将暂存区文件提交到本地仓库  双引号里面填写提交备注
/*
git remote add origin [url]   //将本地仓库添加到远程仓库，如果已经添加可以忽略
*/
git push   //推送本地文件到远程仓库
#git push -u origin master
```

2.clone现有仓库

 git clone 会把Git仓库中的每一个文件的每一个版本都被拉取下来，命令格式是

```
 git clone [url] 
```

```
# url为https格式时
git clone https://github.com/Opithecus/Test_study.git

# url为ssh格式时
git clone git@github.com:Opithecus/Test_study.git

#想要修改文件夹名称 直接在后面加上要修改的名字
git clone git@github.com:Opithecus/Test_study.git workname

git clone -b <分支名> <远程仓库名>    //clone指定分支
```

