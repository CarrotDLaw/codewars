# 544975fc18f47481ba00107b


def circularly_sorted(arr):
    count = 0

    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            count += 1

        if count > 1:
            return False

    if arr[len(arr) - 1] > arr[0] and count != 0:
        return False

    return True
