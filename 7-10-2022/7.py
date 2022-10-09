def swap_case(s):
    li = s.split()
    for i in range(len(li)):
        if li[i].islower():
            c = li[i].upper()
            li.pop(i)
            li.insert(i, c)
        else:
            c = li[i].lower()
            li.pop(i)
            li.insert(i, c)
    s = ''.join(li)
    return s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)