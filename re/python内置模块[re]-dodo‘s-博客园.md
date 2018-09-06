# python内置模块[re]-dodo‘s-博客园

*[Link]* [python内置模块[re]-dodo‘s-博客园](https://www.cnblogs.com/dodoye/p/6218192.html)

---
[dodo](http://www.cnblogs.com/dodoye/)  

[博客园](http://www.cnblogs.com/)   [首页](http://www.cnblogs.com/dodoye/)
[新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
[联系](https://msg.cnblogs.com/send/dodo%E2%80%98s)
[订阅](http://www.cnblogs.com/dodoye/rss)![订阅](//www.cnblogs.com/images/xml.gif)
[管理](https://i.cnblogs.com/)

随笔-12  评论-6  文章-0

# [python内置模块[re]](http://www.cnblogs.com/dodoye/p/6218192.html)

### python内置模块[re]

**re模块：**

python的re模块（Regular
Expression正则表达式）提供各种正则表达式的匹配操作，在文本解析、复杂字符串分析和信息提取时是一个非常有用的工具。

**1、re的简介**

使用python的re模块，尽管不能满足所有复杂的匹配情况，但足够在绝大多数情况下能够有效地实现对复杂字符串的分析提取相关信息。python会将正则表达式转
化为字节码，利用C语言的匹配引擎进行深度优先的匹配。

    import re
    print(re.__doc__)

可以查询re模块的功能信息。

**2、re的正则表达式语法**

**正则表达式的特殊字符：**

特殊字符

意义说明

**'.'**
匹配包括换行符以内的任意一个字符。点号，在普通模式，它匹配除换行符外的任意一个字符。

**'^'**
匹配一个字符串的开始，在 MULTILINE 模式下，也将匹配任意一个新行的开始，尖尖号。

**'$'**
匹配一个字符串的结尾或者字符串最后面的换行符，在 MULTILINE 模式下，也匹配任意一行的行尾，美元符号。

**'*'**
匹配*前面re的重复0次或者任意多次，而且总是试图尽量多次地匹配，星号。

**'+'**
匹配+前面re的重复0次或者1次，如果有的话，也尽量匹配1次，加号。

**'?'**
匹配？前面re的重复0次或者1次，如果有的话，也尽量匹配1次，问号。

***?， +?， ??**
可以看到'*'，'+'和'?'都是贪婪的，但这也许并不是我们说要的，所以，可以在后面加个问号，将策略改为非贪婪，只匹配尽量少的RE，也就是第一个匹配结果。

**{m}**
m是一个数字，匹配**{m}**前面的re重复m次。

**{m,n}**
m和n都是数字，匹配{m,n}前面的RE重复m到n次，例如a{3,5}匹配3到5个连续的a。注意，如果省略m，将匹配0到n个前面的RE；如果省略n，将匹配n
到无穷多个前面的RE；当然中间的逗号是不能省略的，不然就变成前面那种形式了。

**{m,n}?**
{m,n}，也是贪婪的，a{3,5}如果有5个以上连续a的话，会匹配5个，这个也可以通过加问号改变。a{3,5}?如果可能的话，将只匹配3个a。

**'\'**
反斜杆，转义'*'，'?'等特殊字符，或者指定一个特殊序列,强烈建议用raw字符串来表述正则。

**[]**
方括号，用于指定一个字符的集合。可以单独列出字符，也可以用**'-'**连接起止字符以表示一个范围。特殊字符在中括号里将失效，比如[akm$]就表示字符'a
'，'k'，'m'，或'$'，在这里$也变身为普通字符了。[a-z]匹配任意一个小写字母，[a-zA-Z0-9]匹配任意一个字母或数字。如果你要匹配']'或
'-'本身，你需要加反斜杆转义，或者是将其置于中括号的最前面，比如[]]可以匹配']'。还可以对一个字符集合取反，以匹配任意不在这个字符集合里的字符，取反操
作用一个**'^'**放在集合的最前面表示，放在其他地方的'^'将不会起特殊作用。例如[^5]将匹配任意不是'5'的字符；[^^]将匹配任意不是'^'的字符
。**注意：在中括号里+、*、(、)这类字符将会失去特殊含义，仅作为普通字符。反向引用也不能在中括号内使用。**

**'|'**
管道符号，A和B是任意的RE，那么A|B就是匹配A或者B的一个新的RE。任意个数的RE都可以像这样用管道符号间隔连接起来。这种形式可以被用于组中。对于目标字
符串，被'|'分割的RE将**自左至右**一一被测试，一旦有一个测试成功，后面的将不再被测试，即使后面的RE可能可以匹配更长的串，换句话说，'|'操作符是非
贪婪的。要匹配字面意义上的'|'，可以用反斜杆转义：\|，或是包含在反括号内：[|]。

**(...)**
匹配圆括号里的RE匹配的内容，并指定组的开始和结束位置。组里面的内容可以被提取，也可以采用\number这样的特殊序列，被用于后续的匹配。要匹配字面意义上的
'('和')'，可以用反斜杆转义：\\(、\\)，或是包含在反括号内：[(]、[)]。

**(?...)**
这是一个表达式的扩展符号。'?'后的第一个字母决定了整个表达式的语法和含义，除了(?P...)以外，表达式不会产生一个新的组。(?iLmsux)表示'i'、
'L'、'm'、's'、'u'、'x'里的一个或多个字母。表达式不匹配任何字符，但是指定相应的标志：re.I(忽略大小写)、re.L(依赖locale)、r
e.M(多行模式)、re.S(.匹配所有字符)、re.U(依赖Unicode)、re.X(详细模式)。关于各个模式的区别。使用这个语法可以代替在re.com
pile()的时候或者调用的时候指定flag参数。另外，还要注意(?x)标志如果有的话，要放在最前面。

**(?:...)**
匹配内部的RE所匹配的内容，但是不建立组。

**(?P<name>...)**
和普通的圆括号类似，但是子串匹配到的内容将可以用命名的name参数来提取。组的name必须是有效的python标识符，而且在本表达式内不重名。命名了的组和普
通组一样，也用数字来提取，也就是说名字只是个额外的属性。

**(?#...)**
注释，圆括号里的内容会被忽略。

**(?=...)**
如果 ... 匹配接下来的字符，才算匹配，但是并不会消耗任何被匹配的字符。例如 Isaac (?=Asimov) 只会匹配后面跟着 'Asimov' 的
'Isaac '，这个叫做“前瞻断言”。

**(?!...)**
和**(?=...)**相反，只匹配接下来的字符串不匹配 ... 的串，这叫做“反前瞻断言”。

**(?<=...)**
只有当当前位置之前的字符串匹配 ... ，整个匹配才有效，这叫“后顾断言”。字符串'abcdef'可以匹配正则(?<=abc)def，因为会后向查找3个字符
，看是否为abc。所以内置的子RE，需要是固定长度的，比如可以是abc、a|b，但不能是a*、a{3,4}。注意这种RE永远不会匹配到字符串的开头。

**(?<!...)**
这个叫做“反后顾断言”，子RE需要固定长度的，含义是前面的字符串不匹配 ... 整个才算匹配。

**(?(id/name)yes-pattern|no-pattern)**
如有由id或者name指定的组存在的话，将会匹配yes-pattern，否则将会匹配no-pattern，通常情况下no-
pattern也可以省略。例如：(<)?(\w+@\w+(?:\\.\w+)+)(?(1)>)可以匹配 '<user@host.com>' 和
'user@host.com'，但是不会匹配 '<user@host.com'。

**'$'演示**:普通模式下，foo.$去搜索'foo1\nfoo2\n'只会找到'foo2′，但是在 MULTILINE 模式，还能找到 ‘foo1′，而且就用一个 $ 去搜索'foo\n'的话，会找到两个空的匹配：一个是最后的换行符，一个是字符串的结尾。如下演示：

    #'$'演示
    >>> re.findall('(foo.$)', 'foo1\nfoo2\n')
    ['foo2']
    >>> re.findall('(foo.$)', 'foo1\nfoo2\n')
    ['foo2']
    >>> re.findall('(foo.$)', 'foo1\nfoo2\n', **re.MULTILINE**)
    ['foo1', 'foo2']
    >>> re.findall('($)', 'foo\n')
    ['', '']

***?， +?， ??演示：**

    >>> re.findall('<(.*)>', '<H1>title</H1>')
    ['H1>title</H1']
    >>> re.findall('<(.*?)>', '<H1>title</H1>')

    ['H1', '/H1']

    >>> re.search('<(.*)>', '<H1>title</H1>').group()
    '<H1>title</H1>'
    >>> re.search('<(.*?)>', '<H1>title</H1>').group()
    '<H1>'

**(?...)演示：和指定了re.MULTILINE是一样的效果**

    >>> re.findall('(?m)(foo.$)', 'foo1\nfoo2\n')
    ['foo1', 'foo2']

**(?P<name>...)演示：**

    >>> m=re.match('(?P<var>[a-zA-Z_]\w*)', 'abc=123')
    >>> m.group('var') #通过var参数取值
    'abc'
    >>> m.group(1)#通过数字取值
    'abc'
    >>> re.match('<(?P<tagname>\w*)>.*</(?P=tagname)>', '<h1>xxx</h2>')  #这个不匹配
    >>> re.match('<(?P<tagname>\w*)>.*</(?P=tagname)>', '<h1>xxx</h1>')  #这个匹配
    <_sre.SRE_Match object; span=(0, 12), match='<h1>xxx</h1>'>

**(?<=...)演示：**

    >>> m = re.search('(?<=-)\w+', 'spam-egg')
    >>> m.group(0)
    'egg'

**正则表达式特殊序列符号：**

特殊序列符号

意义说明

**\number**
匹配number所指的组相同的字符串。组的序号从1开始。例如：(.+) \1可以匹配'the the'和'55 55'，但不匹配'the end'。这种序列
在一个正则表达式里最多可以有99个，如果number以0开头，或是有3位以上的数字，就会被当做八进制表示的字符了。同时，这个也不能用于方括号内。

**\A**
只匹配字符串的开始。

**\b**
匹配单词边界（包括开始和结束），这里的“单词”，是指连续的字母、数字和下划线组成的字符串。注意，\b的定义是\w和\W的交界，所以精确的定义有赖于UNICO
DE和LOCALE这两个标志位。

**\B**
和\b相反，\B匹配非单词边界。也依赖于UNICODE和LOCALE这两个标志位。

**\d**
相当于[0-9]

**\D**
和\d相反。相当于[^0-9]

**\s**
匹配任何空白字符，等效于[ \t\n\r\f\v]

**\S**
和\s相反，匹配任意非空白字符:[^\t\n\r\r\v]

**\w**
匹配任意数字和字母:[a-zA-Z0-9]

**\W**
和\w相反，匹配任意非数字和字母:[^a-zA-Z0-9]

**\Z**
只匹配字符串的结尾。

**3、re的主要模块功能函数：**

常用的功能函数包括：compile、search、match、split、findall（finditer）、sub（subn）、escape

**compile**

re.compile(pattern[, flags])  
作用：把正则表达式语法转化成正则表达式对象  
flags定义包括：  
re.I：忽略大小写  
re.L：表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境  
re.M：多行模式  
re.S：’ . ’并且包括换行符在内的任意字符（注意：’ . ’不包括换行符）  
re.U： 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库

用了re.compile以后，正则对象会得到保留，这样在需要多次运用这个正则对象的时候，效率会有较大的提升。再用上面用过的例子来演示一下，用相同的正则匹配相
同的字符串，执行100万次，就体现出compile的效率了。

**search**

re.search(pattern, string[, flags])  
search (string[, pos[, endpos]])  
作用：在字符串中查找匹配正则表达式模式的位置，返回 MatchObject 的实例，如果没有找到匹配的位置，则返回 None。

**match**

re.match(pattern, string[, flags])  
match(string[, pos[, endpos]])  
作用：match() 函数只在字符串的开始位置尝试匹配正则表达式，也就是只报告从位置 0 开始的匹配情况，而 search()
函数是扫描整个字符串来查找匹配。如果想要搜索整个字符串来寻找匹配，应当用 search()。

    #!/usr/bin/env python
    import re
    r1 = re.compile(r'world')
    if r1.match('helloworld'):
        print('match succeeds')
    else:
        print('match fails')
    if r1.search('helloworld'):
        print('search succeeds')
    else:
        print('search fails')

说明一下：r是raw(原始)的意思。因为在表示字符串中有一些转义符，如表示回车'\n'。如果要表示\需要写为'\\\'。但如果我就是需要表示一个'\'+'n
'，不用r方式要写为:'\\\n'。但使用r方式则为r'\n'这样清晰多了。

**split**

re.split(pattern, string[, maxsplit=0, flags=0])  
split(string[, maxsplit=0])  
作用：可以将字符串匹配正则表达式的部分割开并返回一个列表。

    #简单IP分析
    #!/usr/bin/env python
    import re
    r1 = re.compile(r'\W+')
    print(r1.split(r'192.168.1.1'))
    print(re.split(r'(\W+)','192.168.1.1'))
    print(re.split(r'(\W+)','192.168.1.1',1))

    #输出结果为：
    ['192', '168', '1', '1']
    ['192', '.', '168', '.', '1', '.', '1']
    ['192', '.', '168.1.1']

用匹配pattern的子串来分割string，如果pattern里使用了圆括号，那么被pattern匹配到的串也将作为返回值列表的一部分。如果maxspli
t不为0，则最多被分割为maxsplit个子串，剩余部分将整个地被返回。

    >>> re.split('\W+', 'Words, words, words.')
    ['Words', 'words', 'words', '']
    >>> re.split('(\W+)', 'Words, words, words.')
    ['Words', ', ', 'words', ', ', 'words', '.', '']
    >>> re.split('\W+', 'Words, words, words.', 1)
    ['Words', 'words, words.']

如果正则有圆括号，并且可以匹配到字符串的开始位置的时候，返回值的第一项，会多出一个空字符串。匹配到字符结尾也是同样的道理：

    >>> re.split('(\W+)', '...words, words...')
    ['', '...', 'words', ', ', 'words', '...', '']

注意，split不会被零长度的正则所分割，将会报FureWarning警告，例如：

    >>> re.split('x*', 'foo')
    C:\Users\Administrator\AppData\Local\Programs\Python\Python35-32\lib\re.py:203:
    FutureWarning: split() requires a non-empty pattern match.
      return _compile(pattern, flags).split(string, maxsplit)
    ['foo']

**findall**

re.findall(pattern, string[, flags])  
findall(string[, pos[, endpos]])  
作用：在字符串中找到正则表达式所匹配的所有子串，并组成一个列表返回。

    #查找[]包括的内容（贪婪和非贪婪查找）
    #!/usr/bin/env python
    import re
    r1 = re.compile(r'([.*])')
    print(re.findall(r1,"hello[hi]heldfsdsf[iwonder]lo"))
    r1 = re.compile(r'([.*?])')
    print(re.findall(r1,"hello[hi]heldfsdsf[iwonder]lo"))
    print(re.findall(r'[0-9]{2}',"fdskfj1323jfkdj"))
    print(re.findall('([0-9][a-z])',"fdskfj1323jfkdj"))
    print(re.findall(r'(?=www)',"afdsfwwwfkdjfsdfsdwww"))
    print(re.findall(r'(?<=www)',"afdsfwwwfkdjfsdfsdwww"))

    #输入结果：
    []
    []
    ['13', '23']
    ['3j']
    ['', '']
    ['', '']

    #这个返回的就是元组的列表
    >>> re.findall('(\d+)\.(\d+)\.(\d+)\.(\d+)', 'My IP is 192.168.0.2, and your is
    192.168.0.3.')
    [('192', '168', '0', '2'), ('192', '168', '0', '3')]

**finditer**

re.finditer(pattern, string[, flags])  
finditer(string[, pos[, endpos]])  
说明：和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并组成一个迭代器返回。

    >>> for m in re.finditer('\w+', 'hello, world!'):
    ...     print(m.group())
    ...
    hello
    world

**sub**

re.sub(pattern, repl, string[, count, flags])  
sub(repl, string[, count=0])  
说明：在字符串 string 中找到匹配正则表达式 pattern 的所有子串，用另一个字符串 repl 进行替换。如果没有找到匹配 pattern
的串，则返回未被修改的 string。Repl 既可以是字符串也可以是一个函数。

    #!/usr/bin/env python
    import re
    p = re.compile('(one|two|three)')
    print(p.sub('num','one word two words three words apple',2))

    #输出结果：
    num word num words three words apple

如果repl是个函数，每次pattern被匹配到的时候，都会被调用一次，传入一个匹配到的MatchObject对象，需要返回一个字符串，在匹配到的位置，就填
入返回的字符串。

    >>> def dashrepl(matchobj):
    ...     if matchobj.group(0) == '-': return ' '
    ...     else:return '-'
    >>> re.sub('-{1,2}', dashrepl, 'pro----gram-files')
    'pro--gram files'

零长度的匹配也会被替换

    >>> re.sub('x*', '-', 'abcxxd')
    '-a-b-c-d-'

特殊地，在替换字符串里，如果有\g这样的写法，将匹配正则的命名组（前面介绍过的，(?P...)这样定义出来的东西）。\g这样的写法，也是数字的组，也就是说，
\g<2>一般和\2是等效的，但是万一你要在\2后面紧接着写上字面意义的0，你就不能写成\20了（因为这代表第20个组），这时候必须写成\g<2>0，另外，
\g<0>代表匹配到的整个子串。

    >>> re.sub('-(\d+)-', '-\g<1>0\g<0>', 'a-11-b-22-c')
    'a-110-11-b-220-22-c'

**subn**  
re.subn(pattern, repl, string[, count, flags])  
subn(repl, string[, count=0])  
说明：该函数的功能和 sub() 相同，只是它返回的是一个元组 (新字符串, 匹配到的次数)。

    >>> re.subn('-(\d+)-', '-\g<1>0\g<0>', 'a-11-b-22-c')
    ('a-110-11-b-220-22-c', 2)

**escape**

把string中，除了字母和数字以外的字符，都加上反斜杆。

    >>> print(re.escape('abc123_@#$'))
    abc123_\@\#\$

**4、编译标志：**

标志

含义

**re.I，**re.IGNORECASE****
让正则表达式忽略大小写，这样一来，[A-Z]也可以匹配小写字母了。此特性和locale无关。

**re.L，**re.LOCALE****
让\w、\W、\b、\B、\s和\S依赖当前的locale。

**re.M，**re.MULTILINE****
影响'^'和'$'的行为，指定了以后，'^'会增加匹配每行的开始（也就是换行符后的位置）；'$'会增加匹配每行的结束（也就是换行符前的位置）。

**re.S，**re.DOTALL****
影响'.'的行为，平时'.'匹配除换行符以外的所有字符，指定了本标志以后，也可以匹配换行符。

**re.U，**re.UNICODE****
让\w、\W、\b、\B、\d、\D、\s和\S依赖Unicode库。

**re.X，**re.VERBOSE****
运用这个标志，你可以写出可读性更好的正则表达式：除了在方括号内的和被反斜杠转义的以外的所有空白字符，都将被忽略，而且每行中，一个正常的井号后的所有字符也被忽
略，这样就可以方便地在正则表达式内部写注释了。

    #下面两个正则表达式是等效的
    a = re.compile(r"""\d +  # the integral part
                       \.    # the decimal point
                       \d *  # some fractional digits""", re.X)
    b = re.compile(r"\d+\.\d*")

**5、方法/属性**

**groups**

RE所含有的组的个数。

**groupindex**

一个mappingproxy字典，定义了命名组的名字和序号之间的关系。

    #这个正则有3个组，如果匹配到，第一个叫区号，最后一个叫分机号，中间的那个未命名

    >>> pattern = re.compile("(?P<quhao>\d+)-(\d+)-(?P<fenjihao>\d+)")
    >>> pattern.groups
    3
    >>> pattern.groupindex
    mappingproxy({'fenjihao': 3, 'quhao': 1})

**pattern**

建立本RE的原始字符串，相当于源代码了，呵呵。

    >>> pattern = re.compile("(?P<quhao>\d+)-(\d+)-(?P<fenjihao>\d+)")
    >>> print(pattern.pattern)
    (?P<quhao>\d+)-(\d+)-(?P<fenjihao>\d+)

**group([group1, ...])**

返回一个或多个子组。如果参数为一个，就返回一个子串；如果参数有多个，就返回多个子串注册的元组。如果不传任何参数，效果和传入一个0一样，将返回整个匹配。如果某
个groupN未匹配到，相应位置会返回None。如果某个groupN是负数或者大于group的总数，则会抛出IndexError异常。

    >>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
    >>> m.group(0) #整个匹配
    'Isaac Newton'
    >>> m.group(1)#第一个子串
    'Isaac'
    >>> m.group(2)#第二个子串
    'Newton'
    >>> m.group(1,2) #多个子串组成元组
    ('Isaac', 'Newton')

如果有其中有用(?P...)这种语法命名过的子串的话，相应的groupN也可以是名字字符串。

    >>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
    >>> m.group('first_name')
    'Malcolm'
    >>> m.group('last_name')
    'Reynolds'

如果某个组被匹配到多次，那么只有最后一次的数据，可以被提取到

    >>> m = re.match(r"(..)+", "a1b2c3")
    >>> m.group(0)
    'a1b2c3'
    >>> m.group(1)
    'c3'
    >>> m.group(2)

**groups([default])**

返回一个由所有匹配到的子串组成的元组。default参数，用于给那些没有匹配到的组做默认值，它的默认值是None

    >>> m = re.match(r"(\d+)\.(\d+)", "24.1632")
    >>> m.groups()
    ('24', '1632')
    #default的作用
    >>> m = re.match(r"(\d+)\.?(\d+)?", "24")
    >>> m.groups() #第二个默认是None
    ('24', None)
    >>> m.groups('0')#现在默认变成0
    ('24', '0')

**groupdict([default])**

返回一个包含所有命名组的名字和子串的字典，default参数，用于给那些没有匹配到的组做默认值，它的默认值是None

    >>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
    >>> m.groupdict()
    {'first_name': 'Malcolm', 'last_name': 'Reynolds'}

**start([group])，**end([group])****

返回的是：被组group匹配到的子串在原字符串中的位置。如果不指定group或group指定为0，则代表整个匹配。如果group未匹配到，则返回 -1。  
对于指定的m和g，m.group(g)和m.string[m.start(g):m.end(g)]等效。  
注意：如果group匹配到空字符串，m.start(group)和m.end(group)将相等

    >>> m = re.search('b(c?)', 'cba')
    >>> m.start(0)
    1
    >>> m.end(0)
    2
    >>> m.start(1)
    2
    >>> m.end(1)
    2

下面是一个把email地址里的“remove_this”去掉的例子

    >>> email = "tony@tiremove_thisger.net"
    >>> m = re.search("remove_this", email)
    >>> email[:m.start()] + email[m.end():]
    'tony@tiger.net'

**span([group])**

返回一个元组： (m.start(group), m.end(group))

**pos**

就是传给RE对象的search()或match()方法的参数pos，代表RE开始搜索字符串的位置。

**endpos**

就是传给RE对象的search()或match()方法的参数endpos，代表RE搜索字符串的结束位置。

**lastindex**

最后一次匹配到的组的数字序号，如果没有匹配到，将得到None。  
例如：(a)b、((a)(b))和((ab))正则去匹配'ab'的话，得到的lastindex为1。而用(a)(b)去匹配'ab'的话，得到的lastind
ex为2。

**lastgroup**

最后一次匹配到的组的名字，如果没有匹配到或者最后的组没有名字，将得到None。

**re**

得到本Match对象的正则表达式对象，也就是执行search()或match()的对象。

**string**

传给search()或match()的字符串。

posted on 2016-12-24 19:28 [dodo‘s](http://www.cnblogs.com/dodoye/) 阅读(...)
评论(...) [编辑](https://i.cnblogs.com/EditPosts.aspx?postid=6218192) 收藏

[刷新评论](javascript:void\(0\);)刷新页面返回顶部

Powered by: [博客园](http://www.cnblogs.com)
模板提供：[沪江博客](http://blog.hjenglish.com) Copyright (C)2018 dodo‘s

