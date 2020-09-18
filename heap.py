'''
Created on Jun 7, 2020

@author: rabel
'''
import math
class Heap:
    
    def __init__(self,array):
        self.array = array
    
    def Heapify(self):
        n = len(self.array)
        mid = math.floor(n/2)   
        for i in range(mid):
            
            Left_c = 2*i+ 1
            Right_c = 2*i + 2
            parent = math.floor(i+1/2)
            if Right_c >= n:
                Right_c = 2*i 
            if Left_c >= n:
                Left_c = 2*i
            if self.array[Right_c] > self.array[parent] :
                self.Swap(Right_c,parent)
                Heap(self.array).Heapify()
            if self.array[Left_c] > self.array[parent]:
                self.Swap(parent,Left_c)
                Heap(self.array).Heapify()
        
           
        return self.array
    def Swap(self,new,old):
        self.array[new],self.array[old] = self.array[old],self.array[new]
    def findMax(self):
        return self.array[0]
    def getHeight(self):
        return math.ceil(math.log(len(self.array)))
    def getLeftChild(self,loc):
        Left_c = 2*loc+ 1
        if loc < math.floor(len(self.array)/2):
            return self.array[Left_c]
        else:
            return "not available"
    def getRightChild(self,loc):
        Right_c = 2*loc+ 2
        if loc < math.floor(len(self.array)/2):
            return self.array[Right_c]
        else:
            return "not available"
    def getParent(self,loc):
        parent = math.floor(loc/2)
        if loc >= 1 and loc <= len(self.array)-1:
            return self.array[parent]
        if loc < 0 or loc > len(self.array):
            return "indefined"
        if loc == 0:
            return "The root does not have a parent" 
    
    def heapSort(self):
        size = len(self.array)
        sort = []
        for i in range(size):
            self.array = self.array[:size] 
            size -= 1
            if self.array[0]> self.array[size]:
                self.Heapify()                     
                self.Swap(0,size)
                sort.insert(i, self.array[size])
            else:
                self.Heapify()
                self.Swap(0,size)
                sort.insert(i, self.array[size])
                
         
        return sort  
             
x = x = [35,33,42,10,14,19,27,44,26,31]
h = Heap(x)  
print(h.Heapify())
p = 0
print('the left child of position ', p, "is: ", h.getLeftChild(p))
"""print("the parent of the child in position ", p, "is ",h.getParent(p) )
print("the height of the tree is: ", h.getHeight())"""
print("the following array was sorted: ", h.heapSort())

            