''' https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1337/
    Design Circular Queue
    Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

    One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

    Implementation the MyCircularQueue class:

    MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    int Front() Gets the front item from the queue. If the queue is empty, return -1.
    int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    boolean isEmpty() Checks whether the circular queue is empty or not.
    boolean isFull() Checks whether the circular queue is full or not.
    You must solve the problem without using the built-in queue data structure in your programming language. '''
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1] * k
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % len(self.queue)
            return True
        return False


    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.queue[self.head] = -1
            self.head = (self.head + 1) % len(self.queue)
            return True
        return False

    def Front(self) -> int:
        return self.queue[self.head]
        

    def Rear(self) -> int:
        return self.queue[self.tail - 1]

    def isEmpty(self) -> bool:
        return self.queue.count(-1) == len(self.queue)

    def isFull(self) -> bool:
        return self.queue.count(-1) == 0        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

def main():
    my_queue = MyCircularQueue(5)
    print('is empty', my_queue.isEmpty())
    print('is full', my_queue.isFull())
    print('after enqueue 1', my_queue.enQueue(1))
    print('after enqueue 2', my_queue.enQueue(2))
    print('after enqueue 3', my_queue.enQueue(3))
    print('is empty', my_queue.isEmpty())
    print('is full', my_queue.isFull())
    print('Front', my_queue.Front())
    print('Rear', my_queue.Rear())
    print('after dequeue', my_queue.deQueue())
    print('Front', my_queue.Front())
    print('Rear', my_queue.Rear())
    print('after enqueue 4', my_queue.enQueue(4))
    print('after enqueue 5', my_queue.enQueue(5))
    print('after enqueue 6', my_queue.enQueue(6))
    print('after enqueue 7', my_queue.enQueue(7))
    print('is empty', my_queue.isEmpty())
    print('is full', my_queue.isFull())
    print('Front', my_queue.Front())
    print('Rear', my_queue.Rear())

if __name__ == '__main__':
    main()
