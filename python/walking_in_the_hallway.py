# 6368426ec94f16a1e7e137fc

def contact(hallway):
    min_d = 10e12
    last_right_arrow = -1

    for i in range(len(hallway)):
        if hallway[i] == ">":
            last_right_arrow = i

        if hallway[i] == "<" and last_right_arrow != -1:
            min_d = min(min_d, i - last_right_arrow)

    if min_d == 10e12:
        return -1

    return (min_d + 1) // 2
