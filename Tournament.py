'''
Created on Jun 20, 2020

@author: rabel
'''
import math 

class Team:
    def __init__(self,name: str,wins: int, loses: int):
        self.name = name
        self.wins = wins
        self.loses = loses
        self. Win = False
        self.Lose = False
        self.winPercentage = float("%.3f" % (self.wins/(self.loses+self.wins)))
        
    def show(self):
        print("This team is the", self.name,"\nhas a record of: ",self.wins,"-",self.loses,"\nWin Pecentage: ",self.winPercentage)
class Braket:
    
    def __init__(self,n):
        self.n = n
        self.braket = []*n
    
    def insertTeam(self,name: str,wins: int, loses: int):
        self.team = Team(name,wins, loses)
        self.braket.append(self.team)
    def organize(self):
        ###usig mergeSort we sort the unsorted array of teams by win percentage
        if self.n > 1:
            mid = math.floor(self.n-1/2)
            lSide = self.braket[:mid]
            rSide = self.braket[mid:]
            lMer = Braket(mid)
            lMer.braket = lSide
            lMer.organize()
            rMer = Braket(mid)
            rMer.braket = rSide
            rMer.organize()
            
            i =k=c=0
            while (i < len(lSide) and k < len(rSide)):
                if (lSide[i].winPercentage > rSide[k].winPercentage):
                   
                    self.braket[c] = lSide[i]
                    i +=1
                else:
                    self.braket[c] = rSide[k] 
                    k += 1
                c += 1
            while i < len(lSide):
                self.braket[c] = lSide[i]
                i += 1
                c += 1
            while k < len(rSide):
                self.braket[c] = rSide[k]
                c += 1
                k += 1
                     
    def printBraket(self):
        for i in range(self.n):
            print(self.braket[i].name)        
            
    def showRecord(self,name):
        for i in range(self.n):
            if self.braket[i].name == name:
                self.braket[i].show()

braket = Braket(8)
braket.insertTeam("Thunder",40,23) 
braket.insertTeam("Mavericks",40,27) 
braket.insertTeam("Grizzlies",32,33) 
braket.insertTeam("Lakers",49,14)
braket.insertTeam("Rockets",40,24)
braket.insertTeam("Nuggets",43,22) 
braket.insertTeam("Jazz",41,23)
braket.insertTeam("Clipers",44,20)
braket.organize()
braket.printBraket()

braket.showRecord("Rockets")

