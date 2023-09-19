class Queue(object):
    def __init__(self, limit=5):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size <= 0

    def enqueue(self, item):
        if self.size >= self.limit:
            self.resize()
        self.que.append(item)
        if self.front is None:
            self.front = 0
        else:
            self.rear = self.size
        self.size += 1
        print('Queue after enqueue:', self.que)

    def dequeue(self):
        if self.size <= 0:
            print('Queue Underflow')
            return 0
        else:
            self.que.pop(0)
            self.size -= 1
            if self.size <= 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
            print('Queue after dequeue:', self.que)

    def queue_rear(self):
        if self.rear is None:
            print("Sorry, the queue is empty!")
            raise IndexError
        return self.que[self.rear]

    def queue_front(self):
        if self.front is None:
            print("Sorry, the queue is empty!")
            raise IndexError
        return self.que[self.front]

    def size(self):
        return self.size

    def resize(self):
        new_que = list(self.que)
        self.limit *= 2
        self.que = new_que


que = Queue()
que.enqueue("first")
print("Front: " + que.queue_front())

que.enqueue("second")
print("Front: " + que.queue_front())
print("Rear: " + que.queue_rear())

que.enqueue("third")
print("Front: " + que.queue_front())
print("Rear: " + que.queue_rear())

que.enqueue("four")
print("Front: " + que.queue_front())
print("Rear: " + que.queue_rear())

que.enqueue("five")
print("Front: " + que.queue_front())
print("Rear: " + que.queue_rear())

que.enqueue("six")
print("Front: " + que.queue_front())
print("Rear: " + que.queue_rear())

que.dequeue()
print("Front: " + que.queue_front())
print("Rear: " + que.queue_rear())

que.dequeue()
print("Front: " + que.queue_front())
print("Rear: " + que.queue_rear())
