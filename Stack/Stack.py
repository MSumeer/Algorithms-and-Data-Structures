class Node:
    def __init__(self, val, prev):
        self.val = val
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, item):
        self.length += 1
        node = Node(val=item, prev=None)
        if(not self.head):
            self.head = node
            return None
        node.prev = self.head
        self.head = node

        return None

    def pop(self):
        if(not self.head):
            return None
        self.length -= 1
        
        HEAD = self.head
        self.head = self.head.prev

        HEAD.prev = None
        
        if (self.length == 0):
            self.head = None

        return HEAD.val

    def peek(self):
        if self.head is not None:
            return self.head.val
        else:
            return None


ex_que = Queue()

ex_que.push(10)
ex_que.push(5)
ex_que.push(2)

print("peek:", ex_que.peek()) # 10

print(ex_que.pop()) # 10
print(ex_que.pop()) # 5
print(ex_que.pop()) # 2
print(ex_que.pop()) # 1