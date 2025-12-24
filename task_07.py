def combine_anagrams(lst):
    d = {}

    for word in lst:
        key = ''.join(sorted(word.lower()))

        if key not in d:
            d[key] = [word]
        else:
            d[key].append(word)

    return list(d.values())


# Тест
print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))