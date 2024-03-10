s = input()
count = 0
res = 0
for i in range(len(s)):
  if s[i] == 'O':
    count += 1
  else:
    res = max(res, count)
    count = 0
else:
  res = max(res, count)
print(res)