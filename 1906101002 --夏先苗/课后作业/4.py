#求数组中的前n个数的平方和：[14,25,98,75,23,1,4,56,59],要求：n需要是input输入，且小于数组长度，不能固定。


L=[14,25,98,75,23,1,4,56,59]
n=int(input('请输入一个数:'))
s=0
if n<len(L) and n>0:
    for n in L:
        s+=n**2
        print(s)
else:
    print('错误')


