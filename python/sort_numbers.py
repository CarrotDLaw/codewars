# 5174a4c0f2769dd8b1000003


def solution(nums):
    if nums is None:
        return []

    for i in range(len(nums)):
        swapped = False
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                swapped = True

        if not swapped:
            break

    return nums
