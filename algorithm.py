# data structure

#STACK  - Activity
#FILO first in last out

class Stack:
    def __init__(self):
        self.items=[]
        
    def push(self,item):
        if item is not None: #item with value none are not allowed
            self.items.append(item)


    def pop(self):
        if len(self.items)> 0:
            item = self.items[-1]
            del self.items[-1]
            return item
        else:
            return None 

stack = Stack()
stack.push(100)
stack.push(None)
stack.push(3)
stack.push(56)

print(stack.items)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

#Queue

#FIFO first in first out

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item): #enqueue adding item
        if item is not None:
            self.items.append(item)

    def dequeue(self): #get item back
        if len(self.items)>0:
            item =self.items[0]
            del self.items[0]
        else:
            return None        

queue = Queue()

queue.enqueue(10)
queue.enqueue(12) 
queue.enqueue(45)

print(queue.items)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())




