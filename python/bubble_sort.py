# 57403b5ad67e87b5e7000d1d


def bubble(lst):
    if lst is None:
        return []

    snapshots = []

    if lst is None:
        return []

    for i in range(len(lst)):
        swapped = False
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
                swapped = True
                snapshots.append(lst.copy())

        if not swapped:
            break

    return snapshots
