# 578fdcfc75ffd1112c0001a1

def bin_rota(arr):
    rows = len(arr)
    cols = len(arr[0])
    rota = []

    for r in range(rows):
        if r % 2 == 0:
            for col in range(cols):
                rota.append(arr[r][col])
        else:
            for col in range(cols - 1, -1, -1):
                rota.append(arr[r][col])

    return rota
