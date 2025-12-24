def multiply_numbers(stroka=None):
  if stroka == None:
    return None
  stroka = str(stroka)
  chislo = 1
  if stroka.isalpha():
    return None
  for chr in stroka:
    if chr in '1234567890':
      chislo *= int(chr)

  return chislo







print(multiply_numbers()) # => None
print(multiply_numbers('ss')) # => None
print(multiply_numbers('1234')) # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3)) # => 6
print(multiply_numbers([5, 6, 4]))