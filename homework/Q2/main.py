from QueueModule import Queue

q = Queue()
print(q.isEmpty())
q.enqueue(1)
print(q.items)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.size())
print(q.items)
print(q.isEmpty())
print(q.dequeue())
print(q.items)