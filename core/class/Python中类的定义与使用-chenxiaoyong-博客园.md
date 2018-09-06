# Python中类的定义与使用-chenxiaoyong-博客园

*[Link]* [Python中类的定义与使用-chenxiaoyong-博客园](https://www.cnblogs.com/chenxiaoyong/p/6279874.html)

---
# [chenxiaoyong](http://www.cnblogs.com/chenxiaoyong/)

随笔 - 44, 文章 - 0, 评论 - 0, 引用 - 0

##  [Python中类的定义与使用](http://www.cnblogs.com/chenxiaoyong/p/6279874.html)

# [Python中类的定义与使用](http://www.cnblogs.com/xkops/p/6269519.html)

目标：

　　1.类的定义

　　2.父类，子类定义，以及子类调用父类

　　3.类的组合使用

　　4.内置功能

1.类的定义

代码如下：

![复制代码](https://common.cnblogs.com/images/copycode.gif)

    #!/usr/bin/env python
    #coding:utf8

    class Hotel(object):
        """docstring for Hotel"""
        def __init__(self, room, cf=1.0, br=15):
            self.room = room
            self.cf = cf
            self.br = br

        def cacl_all(self, days=1):
            return (self.room * self.cf + self.br) * days

    if __name__ == '__main__':
        stdroom = Hotel(200)
        big_room = Hotel(230, 0.9)
        print stdroom.cacl_all()
        print stdroom.cacl_all(2)
        print big_room.cacl_all()
        print big_room.cacl_all(3)

![复制代码](https://common.cnblogs.com/images/copycode.gif)

2.父类、子类以及调用父类

代码如下：

![复制代码](https://common.cnblogs.com/images/copycode.gif)

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 父类
    class AddBook(object):
        def __init__(self, name, phone):
            self.name = name
            self.phone = phone

        def get_phone(self):
            return self.phone

    # 子类，继承
    class EmplEmail(AddBook):
        def __init__(self, nm, ph, email):
            # AddBook.__init__(self, nm, ph) # 调用父类方法一
            super(EmplEmail, self).__init__(nm, ph) # 调用父类方法二
            self.email = email

        def get_email(self):
            return self.email

    # 调用
    if __name__ == "__main__":
        Detian = AddBook('handetian', '18210413001')
        Meng = AddBook('shaomeng', '18210413002')

        print Detian.get_phone()
        print AddBook.get_phone(Meng)

        alice = EmplEmail('alice', '18210418888', 'alice@xkops.com')
        print alice.get_email(), alice.get_phone()

![复制代码](https://common.cnblogs.com/images/copycode.gif)

3.类的组合使用

代码如下：

![复制代码](https://common.cnblogs.com/images/copycode.gif)

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    '''
    1.class类的组合使用
    2.手机、邮箱、QQ等是可以变化的（定义在一起），姓名不可变（单独定义）。
    3.在另一个类中引用
    '''

    class Info(object):
        def __init__(self, phone, email, qq):
            self.phone = phone
            self.email = email
            self.qq = qq

        def get_phone(self):
            return self.phone

        def update_phone(self, newphone):
            self.phone = newphone
            print "手机号更改已更改"

        def get_email(self):
            return self.email

    class AddrBook(object):
        '''docstring for AddBook'''
        def __init__(self, name, phone, email, qq):
            self.name = name
            self.info = Info(phone, email, qq)

    if __name__ == "__main__":
        Detian = AddrBook('handetian', '18210413001', 'detian@xkops.com', '123456')
        print Detian.info.get_phone()
        Detian.info.update_phone(18210413002)
        print Detian.info.get_phone()
        print Detian.info.get_email()

![复制代码](https://common.cnblogs.com/images/copycode.gif)

4.内置功能(函数（）加与不加的区别）

代码如下：

![复制代码](https://common.cnblogs.com/images/copycode.gif)

    #!/usr/bin/env python
    #coding:utf8

    class Books(object):
        def __init__(self, title, author):
            self.title = title
            self.author = author

        def __str__(self):
            return self.title

        def __repr__(self):
            return self.title

        def __call__(self):
            print "%s is written by %s" %(self.title, self.author)

    if __name__ == '__main__':
        pybook = Books('Core Python', 'Wesley')
        print pybook
        pybook()

![复制代码](https://common.cnblogs.com/images/copycode.gif)

\-----------------------------------------------------------------------------
------------------------------------------------------------------------------
-----

![复制代码](https://common.cnblogs.com/images/copycode.gif)

    #!/usr/bin/env python
    #coding:utf8

    class  Number(object):
        """Custum object
        add/radd -> +; 
        sub/rsub -> -;
        mul/rmul -> *;
        div/rdiv -> /;
        """
        def __init__(self, number):
            self.number = number

        def __add__(self, other):
            return self.number + other        

        def __radd__(self, other):
            return self.number  + other

        def __sub__(self, other):
            return self.number - other

        def __rsub__(self, other):
            return other - self.number

        def __gt__(self, other):
            if self.number > other:
                return True
            return False

    if __name__ == '__main__':
        num = Number(10)
        print num + 20
        print 30 + num
        print num - 5
        print 11 - num
        print num > 20

posted on 2017-01-12 21:20
[chenxiaoyong](http://www.cnblogs.com/chenxiaoyong/) 阅读(...) 评论(...)
[编辑](https://i.cnblogs.com/EditPosts.aspx?postid=6279874) 收藏

[刷新评论](javascript:void\(0\);)刷新页面返回顶部

### 导航

  * [博客园](http://www.cnblogs.com/)
  * [首页](http://www.cnblogs.com/chenxiaoyong/)
  * [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
  * [联系](https://msg.cnblogs.com/send/chenxiaoyong)
  *   * [管理](https://i.cnblogs.com/)

### 公告

Powered by:  
[博客园](http://www.cnblogs.com/)  
Copyright (C) chenxiaoyong

