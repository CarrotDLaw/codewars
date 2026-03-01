# 56d5166ec87df55dbe000063


def sum_average(arr):
    sum = 0

    for i in arr:
        small_sum = 0

        for j in i:
            small_sum += j

        small_average = small_sum / len(i)
        sum += small_average

    if sum > 0:
        sum = int(sum)
    elif sum < 0:
        sum = int(sum) - 1

    return sum
