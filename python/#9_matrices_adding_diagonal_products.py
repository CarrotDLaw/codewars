# 590bb735517888ae6b000012


def sum_prod_diags(matrix):
    n = len(matrix)
    sum_1 = 0
    sum_2 = 0

    for start_row in range(n):
        product = 1
        r = start_row
        c = 0

        while r < n and c < n:
            product *= matrix[r][c]
            r += 1
            c += 1

        sum_1 += product

    for start_col in range(1, n):
        product = 1
        r = 0
        c = start_col

        while r < n and c < n:
            product *= matrix[r][c]
            r += 1
            c += 1

        sum_1 += product

    for start_row in range(n):
        product = 1
        r = start_row
        c = n - 1

        while r < n and c >= 0:
            product *= matrix[r][c]
            r += 1
            c -= 1

        sum_2 += product

    for start_col in range(n - 2, -1, -1):
        product = 1
        r = 0
        c = start_col

        while r < n and c >= 0:
            product *= matrix[r][c]
            r += 1
            c -= 1

        sum_2 += product

    return sum_1 - sum_2
