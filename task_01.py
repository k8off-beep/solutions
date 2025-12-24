
def is_palindrome(s1):
    s1 = str(s1)
    s1 = fromating_str(s1)
    if s1 == s1[::-1]:
        return True
    else:
        return False

def fromating_str(s1):
    str = ''
    for i in range(len(s1)):
        if s1[i].lower() in "abcdefghijklmnopqrstuvwxyz1234567890":
            str += s1[i].lower()
    return str



print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
print(is_palindrome("Madam, I'm Adam!")) # => True
print(is_palindrome(333)) # => True
print(is_palindrome(None)) # => False
print(is_palindrome("Abracadabra")) # => False
print(is_palindrome("abra123321arba"))



