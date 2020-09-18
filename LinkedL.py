'''
Created on Jun 16, 2020

@author: rabel
'''

class Node:
    
    def __init__(self,data):
        """creates a new node that has a pointer to the next node"""
        self.data = data 
        self.next = None
class Linked:
     
    def __init__(self):
        self.head = None 
        self.index = None
        """creates an empty Linkedlist"""
        
    def addNode(self,data):
        """ makes the new node object"""  
        node = Node(data) 
        if self.head != None:
            cNode = self.head
            while cNode.next != None:
                cNode = cNode.next
            cNode.next = node
        else:
            """sets the first element as the head, when the list is empty"""
            self.head = node 
    def showLinkedList(self):
        cNode = self.head
        if cNode:
            while cNode:
                print(cNode.data)
                cNode = cNode.next
        else:
            print("list empty")    
    
    def getIndex(self,data):
        cNode = self.head
        self.index = 0
        if cNode:
            while cNode:
                self.index += 1
                if cNode.data == data:
                    print( self.index)
                    break
                else:
                    cNode = cNode.next
                    
LL = Linked()
LL.addNode(4)
LL.addNode(7)
LL.addNode(6)
LL.addNode(5)
LL.showLinkedList()
LL.getIndex(7)

