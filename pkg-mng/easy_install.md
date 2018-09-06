# easy_install

当安装好setuptools/distribute之后，我们就可以直接使用easy_install这个工具了：

1. 从PyPI上安装一个包：当使用 easy_install package 命令后，easy_install 可以自动从 PyPI 上下载相关的包，并完成安装，升级

2. 下载一个包安装：通过 easy_install package.tgz 命令可以安装一个已经下载的包

3. 安装egg文件：通过 easy_install package.egg 可以安装一个egg格式的文件

通过 easy_install --help 命令可以获取该命令相关的帮助提示.

### setuptools/distribute和easy_install之间的关系：

1. setuptools/distribute 都扩展了 distutils，提供了更多的功能
2. easy_install是基于setuptools/distribute的一个工具，方便了包的安装和省级


