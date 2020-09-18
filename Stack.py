'''
Created on Jun 21, 2020

@author: rabel
'''
class Stack:
    
    def __init__(self,n):
        self.n = n 
        self.stack = []*self.n
        self.top = -1
    
    def StackPop(self):
        self.prv = 0
        if self.top <= -1:
            print("your stack is empty!")
        else:
            self.prv = self.stack[self.top]
            self.top -= 1
            self.stack.pop()
    def getPop(self):
        return self.prv       
    def StackPush(self,data):
        if self.top >= self.n - 1:
            print("Your stack is full!")
        else:
            self.top +=1
            self.stack.append(data)

    def showStack(self):
        if self.top > -1:
            print(self.stack)

s = Stack(5)
s.StackPush(12)
s.StackPush(7)
s.StackPop()

s.showStack()