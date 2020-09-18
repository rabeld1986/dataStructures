'''
Created on Jul 7, 2020

@author: rabel
'''

class Queue:
    
    def __init__(self,n):
        self.n = n
        self.queue = []*self.n
        self.top = -1
    def enqueue(self,data):
        self.data = data
        if self.top >= self.n:
            print("Your Queue is full!")
        else:
            self.top +=1
            self.queue.append(self.data)
    def dequeue(self):
        if self.top == -1:
            print("Your Queue is empty!!!")
        else:
            self.queue.pop(0)
    def showQueue(self):
        print(self.queue)
        
    def getRear(self):
        print(self.queue[0])
    def getEnd(self):
        print(self.queue[len(self.queue)-1])

q = Queue(4)
q.enqueue(5)
q.enqueue(4) 
q.enqueue(3)
q.enqueue(77)
q.enqueue(9)
q.showQueue()            
q.getRear()
q.getEnd()