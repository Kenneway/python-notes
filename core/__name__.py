__name__和__main__

__name__：表示模块，类等的名字；
__main__：模块，xxx.py文件本身：
被直接执行时，对应的模块名就是__main__了，可以在
if __name__ == “__main__”:
中添加你自己想要的，用于测试模块，演示模块用法等代码。
作为模块，被别的Python程序导入（import）时，模块名就是本身文件名xxx了。

我们有时写的python模块需要自己测试， 简单方法就是定义main函数， 然后测试自己的模块接口。 
def main():
     test_yourCode()

if __name__ == "__main__":
     main()