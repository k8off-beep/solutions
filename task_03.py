

def max_odd(lst):
    max_num = 0
    for elem in lst:
        if isinstance(elem, (int, float)) and elem % 2 == 1:
            if elem > max_num:
                max_num = elem

    if max_num != 0: return max_num
    else: return None



print(max_odd([1, 2, 3, 4, 4]))  # => 3
print(max_odd([21.0, 2, 3, 4, 4]))  # => 21
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))  # => 3
print(max_odd(['ololo', 'fufufu']))  # => None
print(max_odd([2, 2, 4]))  # => None
