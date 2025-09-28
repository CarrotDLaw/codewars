# 551204b7509063d9ba000b45

def main_diagonal_product(mat):
    product = 1
    for i in range(len(mat)):
        product *= mat[i][i]
    return product
