# anaconda，pycharm，jupyter安装

> anaconda，pycharm，jupyter这三个工具我早已安装，并进行了一定程度的运用

## anaconda
- 运行anaconda prompt创建新环境时，记得使用“管理员身份”运行
- 如果已经安装了pycharn，那么安装anaconda后，可能会出现两个pycharm的情况，一个是我们直接安装的，一个是anaconda安装附带的，要注意区分
- anaconda中自带了jupyter，可以结合使用，效果加倍

## pycharm
- 每创建一个项目，记得创建一个对应的虚拟环境，用于单独存放该项目所需要的包，可以有效区分开各个项目，更加有序清晰
- 合理使用pycharm终端也会大大降低操作的复杂度和难度，不用每一次都使用windows终端

## jupyter
- 该工具在Python基础语法学习、数据分析、机器学习和深度学习中都有大用，可以将代码划分成一段一段的，并且实时给出结果，适合初学者边学边打代码，及时看结果用来改进

---
# GitHub desktop

- 主要是pull、push和commit三个操作
- 在github desktop中创建笔记的方法有两种：
	1. 先创建一份笔记，然后
- 难点主要在于：如何调配obsidian git插件的参数
	要调试的参数如下，可供后续调试参照：
	- Auto commit-and-sync interval (minutes)
	- Auto commit-and-sync after stopping file edits = ON
	- Commit message on auto commit-and-sync = vault backup: {{date}} ({{numFiles}} files)  
	- Pull on startup = ON
	- Push on commit-and-sync = ON
	- Pull on commit-and-sync = ON

- 现在插件已设置为：
  打开笔记后自动 pull + 每隔 3 分钟在你停止编辑后自动 pull → commit → push。

