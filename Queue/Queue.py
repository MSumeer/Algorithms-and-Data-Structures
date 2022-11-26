class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next 

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, item):
        self.length += 1
        node = Node(val=item, next=None)
        if(not self.tail):
            self.tail = self.head = node
        self.tail.next = node
        self.tail = node

        return None

    def dequeue(self):
        if(not self.head):
            return None
        self.length -= 1
        
        HEAD = self.head
        self.head = self.head.next

        HEAD.next = None
        
        if (self.length == 0):
            self.tail = None

        return HEAD.val

    def peek(self):
        if self.head is not None:
            return self.head.val
        else:
            return None


ex_que = Queue()

ex_que.enqueue(10)
ex_que.enqueue(5)
ex_que.enqueue(2)

print("peek:", ex_que.peek()) # 10

print(ex_que.dequeue()) # 10
print(ex_que.dequeue()) # 5
print(ex_que.dequeue()) # 2
print(ex_que.dequeue()) # 1