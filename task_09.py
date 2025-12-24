def connect_dicts(dict1, dict2):
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())

    if sum1 > sum2:
        main_dict = dict1.copy()
        secondary_dict = dict2
    else:
        main_dict = dict2.copy()
        secondary_dict = dict1

    for key, value in secondary_dict.items():
        if key not in main_dict:
            main_dict[key] = value

    result = {key: value for key, value in main_dict.items() if value >= 10}

    sorted_result = dict(sorted(result.items(), key=lambda item: item[1]))

    return sorted_result


print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))  # => {"c": 11, "b": 12}
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))  # => {"d": 11, "c": 12, "a": 13}
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))  # => {"c": 11, "b": 12, "a": 15}