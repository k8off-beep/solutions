def coincidence(lst=None, range_obj=None):
    if lst is None or range_obj is None:
        return []
    
    result = []
    
    for item in lst:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            if range_obj.start <= item < range_obj.stop:
                result.append(item)
    
    return result
print(coincidence([1, 2, 3, 4, 5], range(3, 6)))  # => [3, 4, 5]
print(coincidence())  # => []
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))  # => [1, 2, 2.5]
