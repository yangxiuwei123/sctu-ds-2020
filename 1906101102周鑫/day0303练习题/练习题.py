class Myclass：
'''简单类实例'''
i = 12345
def f（）：
返回'hello world'＃实例化类
x = Myclass（）＃访问类的属性和方法
print（“ Myclass类的属性i为：”，xi）
print（“ Myclass类的方法f输出为：”，xf（））

#实现一个Testclass，包括原始和overturn两个方法
#original方法从a到z打印26个小写英文字母
class Test（）：
def original（self）：
lis = [chr（i）for i in range（97,123）]
print（''。join（lis））
def翻倒（自己）：
print（''。join（[chr（i）for i in range（90,64，-1）]）））
a = Test（）
a.original（）
a.overturn（）


#构造方法（__init __（））
class Test（）：
def __init __（self，a，b）：
print（“已运行”，a + b）
a =测试（10,20）
b = list（[1,2,3]）
打印（b）

#类变量和实例变量区别
#类变量：
a = Test1（）
h = Test1（）
axappend（[1,2,3]）
打印（a，x，b，x）

c = list（）
d = list（）
c.append（[1,2,3]）

#'''类的标准写法'''
class Myclass（）：
def __init __（self，a，b）：
self.x = a
self.y = b
'''继承'''
类parent（）：
def __init __（self）：
self.p ='父类'
def f（）：
print（self.p，'这是爸爸'）
班级孩子（父母）：
def __init __（self）：
self.c ='子类'
def t（）：
print（self.c，'我要继承'）

a = child（）
 在（）
af（）
'''私有公有'''
类测试：
def __init __（self）：
self .__ x = 1
self.y = 2
def __f（self）：
print（'这是密码'）
a = Test（）
打印（a，y）

af（）
a .__ f（）
'''参数传递'''
class Test1（）：
def __init __（self）：
self.t1 ='父类'
def f（）：
return'爸爸'
class Test2（）：
def __init __（self）：
self.t2 ='子类'
def f（self，object）：
print（object，f（））
a = Test1（）
b = Test2（）
bf（a）
def main（object）：
print（object，f（））
返回'123'
打印（main（a））