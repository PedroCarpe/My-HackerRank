def mini_max_sum(arr):
    mini_sum = 0
    max_sum = 0
    arr_copy = arr.copy()

    arr.remove(max(arr))
    mini_sum = sum(arr)

    arr_copy.remove(min(arr_copy))
    max_sum = sum(arr_copy)

    print(f'{mini_sum} {max_sum}')

mini_max_sum([1,2,3,4,5])    