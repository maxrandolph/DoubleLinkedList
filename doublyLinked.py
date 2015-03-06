"""
Max Randolph
Spring 2015
"""
import sys
class Node(object):
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
    def __iter__(self):
        yield self.data
        yield self.next
        yield self.prev

    def __str__(self):
        return str(self.data)
spot=Node(0)
class DoubleLinkedList(object):
    head = None
    tail = None
    
    def __init__(self,sourceCollection=None):
        self._size=0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
        self._items=None
        
    def __iter__(self):
       
        
        cursor=self.head
        for count in range(0,self._size):
            yield cursor.data
            cursor=cursor.next
    def __str__(self):
        return "->"+"<->".join(map(str,self))+"<->"
    def add(self,elem):
        self._size+=1
        newNode=Node(elem)
        
        if self.head==None:
            self.tail=newNode
            self.head=self.tail
        else:
            newNode.next=self.head
            newNode.prev=self.tail
            self.tail.next=newNode
            self.tail = newNode
        self.head.prev=self.tail    
        

    def clear(self):
        self._size=0
        self.head=None

def main():
    doublyList=DoubleLinkedList()
    n=0
    howBig=input()             #first line of input = n/length of DoubleLinkedList
    howManyForward=input()     #second line of input will = how many nodes to traverse when the m command is issued
    howManyBackwards=input()   #Same, except this is how many will traverse when direction = 1(go backwards)
    routine=input()            #Accepts the string that is the map for the loop. 
    routine=routine.lower()    #lowercase the string so that there won't have to be a case sensitive check
    routineList=list(routine)  #split the string into individual letters so the loop can easily go through each letter.
    howBig=int(howBig)         #turn the first line into an integer so it can be used in other places
    howManyForward=int(howManyForward)      #integerize the second line
    howManyBackwards=int(howManyBackwards)  #integerize the third line of input
    
    for x in range(0,howBig+1): #Okay, this should be O(N) time.
        doublyList.add(n)       #For the size of n, add a node with n's value.
        n+=1
    
    #print(doublyList)#print the initial doubly linked list
    
    cursor=doublyList.head    #create a cursor node. NODE ~~~~~~~~~~~~~~~~~~~~
    direction=0               #direction variable
    n=0
    a=routineList[n]          #set the command variable = to the first letter of the command string
    n+=1                      #add one to n so the next command will be lined up ready to go.
    initialN=doublyList._size #sets a variable to hold a value of the length of the list so that it does not vary with _size
    while a !="x":            #basically the same as saying while==True
        if a == "m":          
            if direction == 0:                     #if direction is 0, go forward when moving, otherwise, go backwards
                for k in range(0,howManyForward):  #this loop is not nested, so it will also be O(n) not a big time commitment
                    cursor = cursor.next           #unnecessary node here, but
                    doublyList.head=cursor
                #print(doublyList)
            else:
                for k in range(0,howManyBackwards):
                    cursor = cursor.prev
                    doublyList.head=cursor
                #print(doublyList)
        if a == "t":#Change direction that the node list is processed in
            if direction ==0: 
                direction=1
                #print(doublyList)
                a="switch"
            else:
                direction=0 
                #print(doublyList)
                a="switch"
        if a == "i": #increment value at head node
            doublyList.head.data=(doublyList.head.data+1)%(initialN)
            #print(doublyList)
        if a == "d":#decrement value at head node
            doublyList.head.data=(doublyList.head.data-1)%(initialN-1)
            #print(doublyList)
        if a == "r":#remove node at head value and move according to direction variable
            if doublyList._size>1:
                cursor.prev.next=cursor.next
                cursor.next.prev=cursor.prev
                if direction == 0: cursor = cursor.prev
                if direction == 1: cursor = cursor.next
                doublyList.head=cursor
                doublyList._size-=1
                #print(doublyList)
            else:
                print(doublyList.head.data)
                exit()
        if a == "c":#copy node at head position and insert it depending on direction
            if direction == 0:
                newNode=Node(doublyList.head.data,doublyList.head,doublyList.head.prev)
                doublyList.head.prev.next=newNode
                doublyList.head.prev=newNode
            else:
                newNode=Node(doublyList.head.data,doublyList.head.next,doublyList.head)
                doublyList.head.next.prev=newNode
                doublyList.head.next=newNode
                
            doublyList._size+=1
            #print(doublyList)
        
        if n<len(routineList):
            a=routineList[n]
            n+=1
        else:
            n=0
            a=routineList[n]
            n+=1
main()
