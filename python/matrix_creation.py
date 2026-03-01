# 5a34da5dee1aae516d00004a


def get_matrix(n):
    mat = []

    for i in range(n):
        row = [0] * n
        row[i] = 1
        mat.append(row)

    return mat
