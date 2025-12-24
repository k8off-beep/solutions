def sort_list(lst):
    if len(lst) == 0:
        return []
    max_num = max(lst)
    min_num = min(lst)
    for i in range(len(lst)):
        if lst[i] == min_num:
            lst[i] = max_num
        elif lst[i] == max_num:
            lst[i] = min_num

    lst.append(min_num)
    return lst





print(sort_list([])) # => []
print(sort_list([2, 4, 6, 8])) # => [8, 4, 6, 2, 2]
print(sort_list([1])) # => [1, 1]
print(sort_list([1, 2, 1, 3])) # => [3, 2, 3, 1, 1]