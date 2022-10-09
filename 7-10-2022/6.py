# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
if __name__ == '__main__':
    N = int(input())
    li = []
    for _ in range(N):
        command = input().split()
        if command[0] == 'append':
            li.append(int(command[1]))
        elif command[0] == 'insert':
            li.insert(int(command[2]), int(command[1]))
        elif command[0] == 'print':
            print(li)
        elif command[0] == 'remove':
            li.remove(int(command[1]))
        elif command[0] == 'sort':
            li.sort()
        elif command[0] == 'pop':
            li.pop()
        elif command[0] == 'reverse':
            li.reverse()


