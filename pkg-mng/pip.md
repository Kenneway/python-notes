# pip

pip是目前最流行的Python包管理工具，它被当作easy_install的替代品，但是仍有大量的功能建立在setuptools之上。

easy_install 有很多不足：安装事务是非原子操作，只支持 svn，没有提供卸载命令， 安装一系列包时需要写脚本。pip 解决了以上问题，已经成为新的事实标准。

pip的使用非常简单，并支持从任意能够通过 VCS 或浏览器访问到的地址安装 Python 包：

	安装:  pip install SomePackage 
	卸载:  pip uninstall SomePackage 

文章的下面部分就重点介绍一下pip相关的内容。


### 使用pip

在大家使用Python中，推荐使用pip进行Python包管理，pip的安装和使用都比较方便。


### pip安装

pip的安装有两种常用的方式：

1. 下载get-pip.py文件，然后执行 python get-pip.py 进行安装（如果没有安装setuptools，那么get-pip.py会帮忙安装）
2. 现在pip源码包，然后通过setup.py进行安装


### pip常用命令

对于pip，最常用的肯定还是 pip --help ，通过帮助文档，就可以大概知道如何使用命令和参数。

	# 从PyPI安装软件包
	pip install SomePackage

	# 卸载软件包
	pip uninstall SomePackage

	# 查看以安装软件包
	pip list

	# 查看可升级软件包
	pip list --outdated

	# 升级软件包
	pip install --upgrade SomePackage

	# 查看软件包安装了哪些文件及路径等信息
	pip show --files SomePackage

	# 安装软件包的指定版本号
	# latest version
	pip install SomePackage

	# specific version
	pip install SomePackage==1.0.4

	# minimum version
	pip install 'SomePackage>=1.0.4'

	# 根据依赖文件安装软件包
	# 使用pip导出依赖文件列表
	pip freeze > requirements.txt

	# 根据依赖文件列表，自动安装对应的软件包
	pip install -r requirements.txt


