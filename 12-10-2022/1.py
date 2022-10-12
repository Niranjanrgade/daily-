def calculate_covariance(array1, array2):
    def avg(arr):
        sum_of_ele = 0
        for ele in arr:
            sum_of_ele += ele
        avg_arr = sum_of_ele / len(arr)
        return avg_arr

    avg_array1 = avg(array1)
    avg_array2 = avg(array2)

    def diff(arr, mean):
        diff_arr = []
        for ele in arr:
            diff_arr.append(ele - mean)
        return diff_arr

    diff_arr1 = diff(array1, avg_array1)
    diff_arr2 = diff(array2, avg_array2)

    mul_arr = []

    for ele1, ele2 in zip(diff_arr1, diff_arr2):
        mul_arr.append(ele1 * ele2)

    covariance = avg(mul_arr)
    return covariance


array1 = [10, 15, 18, 20, 25]
array2 = [18, 20, 30, 35, 40]

print(calculate_covariance(array1, array2))