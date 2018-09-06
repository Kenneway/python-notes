### easy_install卸载

通过easy_install 安装的模块可以直接通过以下命令卸载

	easy_install -m PackageName
	
然后删除\Python27\Lib\site-packages目录下的egg。


### setup.py卸载

通过发行包附带的setup.py安装的模块，首选setup.py提供的uninstall选项。

如果作者没有提供uninstall选项，则通过如下命令行手动卸载：

首先获取安装过程中产生的文件：

	python setup.py install --record record.txt

然后干掉它们：
	
	FOR /F "delims=" %f in (record.txt) DO del "%f"

之后可以去\Python27\Lib\site-packages检查有无空目录残留。


### pip卸载

安装pip

	wget https://bootstrap.pypa.io/get-pip.py
	python get-pip.py 

--------------------------------------------------------------------

删除指定的模块或者包
	
	pip uninstall xxx

我觉得还是尽量用easy_install来安装，这样卸载起来比较方便。

--------------------------------------------------------------------

卸载所有pip的包：

	pip freeze | grep -v "^-e" | xargs pip uninstall -y


