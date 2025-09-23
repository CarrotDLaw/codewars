# 54da539698b8a2ad76000228

def is_valid_walk(walk):
    if len(walk) != 10:
        return False

    x = 0
    y = 0

    for d in walk:
        if d == "n":
            y += 1
        elif d == "s":
            y -= 1
        elif d == "e":
            x += 1
        elif d == "w":
            x -= 1

    if x == 0 and y == 0:
        return True

    return False
