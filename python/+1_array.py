# 5514e5b77e6b2f38e0000ca9


def up_array(arr):
    if not arr:
        return None

    num = 0
    for digit in arr:
        if digit < 0 or digit > 9:
            return None

        num = num * 10 + digit

    num += 1

    result = []
    while num > 0:
        result.insert(0, num % 10)
        num //= 10

    if len(result) > len(arr):
        return result

    zeros_needed = len(arr) - len(result)
    for i in range(zeros_needed):
        result.insert(0, 0)

    return result
