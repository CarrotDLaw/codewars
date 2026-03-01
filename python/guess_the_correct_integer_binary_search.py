# 5749b2fc8bf8b6fbd3001ff3


def find_secret_number(low, high, guess_bot):
    left = low
    right = high

    while left <= right:
        mid = left + (right - left) // 2
        response = guess_bot.guess_number(mid)

        if response == "Correct":
            return mid
        elif response == "Smaller":
            right = mid - 1
        elif response == "Larger":
            left = mid + 1

    return None
