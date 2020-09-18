'''
Created on Jun 25, 2020

@author: rabel
'''
### for this example will use an object containing the information of customers bank info
class Client:
    def __init__(self,name: str, accNum: int , balance: int):
        self.name = name
        self.accNum = accNum
        self.balance = balance
        self.chainNext = None
        self.Ckey = None
    def showInfo(self):
        print("Costumer Name: ", self.name,"\n Account Num: ",self.accNum,"\n Current Bal: $", self.balance)    
class HashTable:
    
    def __init__(self,n: int):
        self.n = n 
        self.Table = [[] for _ in range(self.n)]

    def Hash(self,dat: Client):
        self.dat = dat
        self.key = 0
        otherSum = 0
        for i in range(len(dat.name)):
            if  dat.name[i]== " ":
                otherSum = 0
            else:
                self.key += ord(dat.name[i])   
        self.index = self.key % self.n
        self.dat.Ckey = self.key
        
        self.Table[self.index].append( self.dat)
        
        
    def Search(self,key):
        index = key % self.n
        for i in range(len(self.Table[index])):
            Cl_info = self.Table[index][i].showInfo()
        print(Cl_info,"\nlocated in index: ",index)        
    def Delete(self,key):
        index = key % self.n
        self.Table[index].pop()
        print("The Client:at index ",index," was deleted!")
    def ShowHash(self):
        print(self.Table)
                  
c1 = Client("John Smith",1111110,500) 
c2 = Client("Helen James",1234567,1000)
c3 = Client("Mary Quinn",5543297,200)
c4 = Client("John Smith",7896455,7000)
c5 = Client("John Smith",1500372,600)
c6 = Client("John Smith",4533229,1100)
H = HashTable(5)
H.Hash(c1)
H.Hash(c2)
H.Hash(c3)
H.Hash(c4)
H.Hash(c5)
H.Hash(c6)
H.Search(c2.Ckey)
H.ShowHash()