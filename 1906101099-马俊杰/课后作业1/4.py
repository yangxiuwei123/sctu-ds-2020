#4、	求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59]
#要求：n需要是input输入，且小于数组长度，不能固定。

l=[14,25,98,75,23,1,4,56,59]
a=int(input('输入需要的数组长度：'))
b=list(l[:a])
x=0
for i in b:
    x=x+i**2
print(x)