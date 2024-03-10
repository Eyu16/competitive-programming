n = int(input())
for _ in range(n):
  w = input()
  i = 0
  j = len(w) - 1
  count = 0
  while i < j:
    if w[i] != w[j]:
      count += 1
    i += 1
    j -= 1
  print(count)
    