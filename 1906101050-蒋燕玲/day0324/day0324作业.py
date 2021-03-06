'''给定一个不为空的链表，要求找到该链表的中间节点（若有两个中间值取第二个），然后输出中间值往后的链表
例如：[1，2，3，4，5]
输出：[3，4，5]
思路1：先找到链表的长度，然后找到中间位置，最后将链表的头节点指向中间位置的节点
还可以使用其他思路，可跟据自己的需求编写代码'''
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkNode():
    def __init__(self):
        self.head = Node(-1)
    def insert_tail(self,date):#尾插法
        tail = self.head.next
        for i in date:
            node = Node(i)
            if tail is None:
                self.head.next = node
                tail = node
            else:
                tail.next = node
                tail = node

a = LinkNode()
l = list(map(int,input().split()))
a.insert_tail(l)
p = a.head
res = []
count = 0
while p.next != None:
    p = p.next
    res.append(p.value)
    count += 1
print(res[count//2:])