import re
def count_words(str):
    clean_text = re.sub(r'[^\w\s]', '', str.lower())
    words = clean_text.split()
    slovar = {}
    for wrd in words:
        if wrd not in slovar:
            slovar[wrd] = 1
        else:
            slovar[wrd] += 1
    return slovar






print(count_words("A man,  a plan, a canal -- Panama")) # => {"a": 3, "man": 1,
#"canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo")) # => {"doo": 3, "bee": 2}

