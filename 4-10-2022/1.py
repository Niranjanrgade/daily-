def two_sum(input_given, output_given):
    li1 = [i for i in input_given[::2]]
    li2 = [j for j in input_given[1::2]]
    for k in range(len(li1)):
        if output_given == li1[k] + li2[k]:
            print('found')
            break
        else:
            two_sum(li1, output_given)
            two_sum(li2, output_given)


two_sum(, 9)