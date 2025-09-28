# 526233aefd4764272800036f

def matrix_addition(a, b):
    n = len(a)
    mat = []
    
    for i in range(n):
        row = [0] * n
        
        for j in range(n):
            row[j] = a[i][j] + b[i][j]
            
        mat.append(row)
        
    return mat
