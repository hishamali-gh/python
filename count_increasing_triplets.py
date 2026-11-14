def count_increasing_triplets(arr):
    arr_sorted = [*sorted(arr)]
    arr_unique = [arr_sorted[0]]

    for i in range(1, len(arr_sorted)):
        for j in range(len(arr_unique)):
            if arr_sorted[i] == arr_unique[j]:
                break

        else:
            arr_unique += [arr_sorted[i]]

    del arr_sorted

    n = 0

    for _ in arr_unique:
        n += 1

    count = 0

    # Solution logic here

arr = [1, 2, 3, 4, 1]

count_increasing_triplets(arr)
