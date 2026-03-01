# 5893eb36779ce5faab0000da


def matrix_elements_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_price = 0

    for j in range(cols):
        for i in range(rows):
            if matrix[i][j] == 0:
                break

            total_price += matrix[i][j]

    return total_price
