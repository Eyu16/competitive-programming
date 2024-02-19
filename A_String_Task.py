s = input().lower()
result = ""
vowels = {'a','e','i','o','u','y'}
for char in s:
  if char not in vowels:
    result += '.'
    result += char
    
print(result)
  