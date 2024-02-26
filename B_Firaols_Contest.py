from collections import defaultdict
n, m = map(int, input().split())
difficulties = list(input().split())
dicti = defaultdict(int)
count = 0
res = ""
for diff in difficulties:
  if dicti[diff] == 0:
    count += 1
    if count == n:
      res += '1'
      count = 0
      for key in dicti:
        if dicti[key] - 1 > 0:
          count += 1
        if dicti[key] > 0:
          dicti[key] -= 1
    else:
      res += '0'
      dicti[diff] = 1
  else:
    res += '0'
    dicti[diff] += 1
      
print(res)
    