class Stack:
    def __init__(self):
        self.li = []

    def push(self, ele):
        self.li.append(ele)
        print(f"{ele} pushed in stack")

    def pop(self):
        try:
            popped_ele = self.li.pop()
            print(f"{popped_ele} popped from stack")
        except IndexError:
            print("Stack is empty!")

    def print_stack(self):
        print(self.li)


class Queue:
    def __init__(self):
        self.li = []

    def enqueue(self, ele):
        self.li.append(ele)
        print(f"{ele} enqueued in queue")

    def dequeue(self):
        try:
            dequeued_ele = self.li.pop(0)
            print(f"{dequeued_ele} dequeued from queue")

        except IndexError:
            print("Queue is empty!")

    def print_queue(self):
        print(self.li)


class Deque:
    def __init__(self):
        self.li = []

    def enqueue_from_right(self, ele):
        self.li.append(ele)
        print(self.li)

    def enqueue_from_left(self, ele):
        self.li.insert(0, ele)
        print(self.li)

    def dequeue_from_right(self):
        try:
            self.li.pop()
            print(self.li)
        except IndexError:
            print("Deque is empty!")

    def dequeue_from_left(self):
        try:
            self.li.pop(0)
            print(self.li)
        except IndexError:
            print("Deque is empty!")

    def print_deque(self):
        print(self.li)


def print_menu():
    print('PRESS')
    print('1. Stack')
    print('2. Queue')
    print('3. Deque')
    print('4. Exit')
    ch = int(input("Enter your choice..."))
    return ch


def print_stack_menu():
    print('PRESS')
    print('1. To push element in stack')
    print('2. To pop element from stack')
    print('3. To print stack')
    print('4. Exit')
    ch = int(input("Enter your choice..."))
    return ch


def print_queue_menu():
    print('PRESS')
    print('1. To enqueue element in queue')
    print('2. To dequeue element from queue')
    print('3. To print queue')
    print('4. Exit')
    ch = int(input("Enter your choice..."))
    return ch


def print_deque_menu():
    print('PRESS')
    print('1. To enqueue element in queue from right')
    print('2. To enqueue element in queue from left')

    print('3. To dequeue element from queue from right')
    print('4. To dequeue element from queue from left')

    print('5. To print queue')
    print('6. Exit')
    ch = int(input("Enter your choice..."))
    return ch


while True:
    choice = print_menu()
    if choice == 1:
        stack = Stack()
        while True:
            stack_choice = print_stack_menu()
            if stack_choice == 1:
                value = input("Element to push: ")
                stack.push(value)
            elif stack_choice == 2:
                stack.pop()
            elif stack_choice == 3:
                stack.print_stack()
            elif stack_choice == 4:
                break

    elif choice == 2:
        queue = Queue()
        while True:
            queue_choice = print_queue_menu()
            if queue_choice == 1:
                value = input("Element to enqueue: ")
                queue.enqueue(value)
            elif queue_choice == 2:
                queue.dequeue()
            elif queue_choice == 3:
                queue.print_queue()
            elif queue_choice == 4:
                break

    elif choice == 3:
        deque = Deque()
        while True:
            deque_choice = print_deque_menu()
            if deque_choice == 1:
                value = input("Element to enqueue: ")
                deque.enqueue_from_right(value)
            elif deque_choice == 2:
                value = input("Element to enqueue: ")
                deque.enqueue_from_left(value)
            elif deque_choice == 3:
                deque.dequeue_from_right()
            elif deque_choice == 4:
                deque.dequeue_from_left()
            elif deque_choice == 5:
                deque.print_deque()
            elif deque_choice == 6:
                break

    elif choice == 4:
        break
