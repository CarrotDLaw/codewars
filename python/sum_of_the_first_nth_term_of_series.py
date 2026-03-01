# 555eded1ad94b00403000071


def series_sum(n):
    if n == 0:
        return "0.00"

    sum = 0

    for i in range(n):
        a = 1 / (3 * i + 1)
        sum += a

    return f"{sum:.2f}"
