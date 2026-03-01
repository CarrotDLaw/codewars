# 5526fc09a1bbd946250002dc


def find_outlier(integers):
    for i in range(len(integers) - 1):
        parity_1 = integers[i - 1] % 2
        parity_2 = integers[i] % 2

        if parity_1 != parity_2:
            parity_3 = integers[i + 1] % 2

            return (
                integers[i - 1] if parity_2 == parity_3 else integers[i]
            )

    return integers[len(integers) - 1]
