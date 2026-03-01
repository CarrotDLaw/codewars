# 691ca4c58c5f7e662d508d31


def find_saddle_points(matrix) -> list[tuple[int, int]]:
    row_mins: list[tuple[int, int]] = []
    for i in range(len(matrix)):
        row_min = matrix[i][0]
        for j in range(1, len(matrix[i])):
            if matrix[i][j] < row_min:
                row_min = matrix[i][j]
        row_mins.append(row_min)

    col_maxs: list[tuple[int, int]] = []
    for i in range(len(matrix[0])):
        col_max = matrix[0][i]
        for j in range(1, len(matrix)):
            if matrix[j][i] > col_max:
                col_max = matrix[j][i]
        col_maxs.append(col_max)

    saddle_points: list[tuple[int, int]] = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            p = matrix[i][j]
            if row_mins[i] == p and col_maxs[j] == p:
                saddle_points.append((i, j))

    return saddle_points
