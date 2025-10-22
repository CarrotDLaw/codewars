# 52fba2a9adcd10b34300094c

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = []

    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        new_matrix.append(new_row)

    return new_matrix
