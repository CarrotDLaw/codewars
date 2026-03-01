# 5b4e779c578c6a898e0005c5


def draw_stairs(n):
    s = ""

    for i in range(n):
        for _ in range(i):
            s += " "

        s += "I"

        if i == n - 1:
            break

        s += "\n"

    return s
