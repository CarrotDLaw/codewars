# 581214d54624a8232100005f

def matrix(array):
    for i in range(len(array)):
        if array[i][i] < 0:
            array[i][i] = 0
        else:
            array[i][i] = 1

    return array
