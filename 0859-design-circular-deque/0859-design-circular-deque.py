class MyCircularDeque:
    def __init__(self, k):
        self.deque = [0] * k 
        self.front = 0
        self.rear = 0
        self.capacity = k
        self.size = 0   

    def insertFront(self, value) :
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.capacity
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) :
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) :
        return self.size == 0

    def isFull(self) :
        return self.size == self.capacity
