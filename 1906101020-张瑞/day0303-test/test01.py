class MyClass():
#()可以不要
    i=123456
    def f(self,ostr):
        print(ostr)

x=MyClass()
print(x.i,x.f('hello,world'))