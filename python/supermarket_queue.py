# 57b06f90e298a7b53d000a86


def hasPositive(arr) -> bool:
    for i in arr:
        if i > 0:
            return True

    return False


def nonZeroElements(arr) -> list[int]:
    result: list[int] = []

    for i in arr:
        if i > 0:
            result.append(i)

    return result


def queue_time(customers, n):
    cashiers: list[int] = [0] * n
    total_time = 0

    while customers or hasPositive(cashiers):
        for i in range(n):
            if cashiers[i] == 0 and customers:
                cashiers[i] = customers.pop(0)

        if not hasPositive(cashiers) and not customers:
            break

        occupied_cashiers: list[int] = nonZeroElements(cashiers)
        step = min(occupied_cashiers)

        for i in range(n):
            if cashiers[i] > 0:
                cashiers[i] -= step

        total_time += step

    return total_time
