
class Node:
    def __init__(self):
        self.left = None
        self.value = None
        self.right = None

    def get_left_node(self):
        return self.left

    def get_value(self):
        return self.value

    def get_right(self):
        return self.right

    def go_to_left(self):
        node = Node()

    def go_to_right(self):
        node = Node()


def print_binary_tree_menu():
    print("PRESS")
    print('1. To get value at node')
    print('2. To get value at left node')
    print('3. To get value at right node')
    print('4. To go to the left node')
    print('5. To go to the left node')
    print('6. To add value in Binary tree')
    print('7. Exit')
    ch = int(input("Enter your choice..."))
    return ch


while True:
    choice = print_binary_tree_menu()
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
    elif choice == 7:
        break