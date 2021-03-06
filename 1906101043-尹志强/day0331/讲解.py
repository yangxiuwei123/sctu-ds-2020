class Solution:
    def middleNode(self, head):
        cur=head
        num=0
        while cur :
            num=num+1
            cur=cur.next
        mid=num//2
        new_head=head
        for i in range(mid):
            new_head=new_head.next
        return new_head



class Stack():
    def __init__(self,limit=10):
        self.stack=[]
        self.limit=limit
    def is_empty(self):
        return len(self.stack)==0
    def push(self,data):
        if len(self.stack)>=self.limit:
            print('栈溢出')
        else:
            self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print('空栈不能被弹出')
    def top(self):
        if self.stack:
            return self.stack[-1]
    def size(self):
        return len(self.stack)


stack=Stack()
print(stack.size())
stack.push(1)
stack.push(2)
print(stack.size())
