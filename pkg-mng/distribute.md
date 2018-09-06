distribute是setuptools的一个分支版本。分支的原因是有一部分开发者认为 setuptools 开发太慢。但现在，distribute 又合并回了 setuptools 中，所以可以认为它们是同一个东西。

前面看到setup.py可以创建一个压缩包，而setuptools使用了一种新的文件格式（.egg），可以为Python包创建 egg文件。setuptools 可以识别.egg文件，并解析、安装它


