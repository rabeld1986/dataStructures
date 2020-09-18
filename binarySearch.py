'''
Created on Jun 3, 2020

@author: rabel
'''
import math
class BinarySearch:
    
    def __init__(self,Array,target):
        self.Array = Array
        self.target = target
     
    def Search(self):
        Left_el = 0
        Right_el = len(self.Array) - 1
        mid = math.floor(Left_el+Right_el/2)
        while (Left_el < Right_el):
            if (self.Array[mid] < self.target):
                mid = mid + 1
            elif (self.Array[mid] > self.target):
                mid = mid - 1
            
            else:
                return mid
        print( "not found!")
    def getFirst(self):
        return self.Array[0]
    def getLast(self):
        return self.Array[self.len(self.Array)-1]
    

A = [1,3,6,17,25,60,75,88,102,120]
tar = 102
    
b = BinarySearch(A,tar)
print(b.Search())
          
    
    
    
    
    
    
    
    
        