# 64c743cb0a2a00002856ff73


def switch_gravity(lst):
    rows = len(lst)
    cols = len(lst[0])

    for col in range(cols):
        blocks = 0
        for row in range(rows):
            if lst[row][col] == "#":
                blocks += 1

        for row in range(rows):
            lst[row][col] = "-"

        for i in range(blocks):
            lst[rows - 1 - i][col] = "#"

    return lst
