'''
Created on Jun 3, 2020

@author: rabel
'''
import math
class MergeSort:
     
    def __init__(self,Array):
        self.Array = Array
         
    def merge(self):
        n = len(self.Array)
        if (n>1):            
            
            mid = math.floor(n - 1 /2) 
            L_ar = self.Array[:mid]
            R_ar = self.Array[mid:]
            Left_merge = MergeSort(L_ar)
            Left_merge.merge()
            Right_merge = MergeSort(R_ar) 
            Right_merge.merge()
            i =k=c=0
            while (i < len(L_ar) and k < len(R_ar)):
                if (L_ar[i] < R_ar[k]):
                   
                    self.Array[c] = L_ar[i]
                    i +=1
                else:
                    self.Array[c] = R_ar[k]  
                    k += 1
                c += 1
            while i < len(L_ar):
                self.Array[c] = L_ar[i]
                i += 1
                c += 1
            while k < len(R_ar):
                self.Array[c] = R_ar[k]
                c += 1
                k += 1
        return self.Array               
                   
x = [17,6,60,55,4,70,15,25] 
ms = MergeSort(x).merge()
print(ms)  


                 
                    
                    
                
                
                