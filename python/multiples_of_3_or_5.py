# 5648b12ce68d9daa6b000099


def solution(number):
    if number <= 0:
        return 0

    sum = 0
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            sum += n

    return sum
