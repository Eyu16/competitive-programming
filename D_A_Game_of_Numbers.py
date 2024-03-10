t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  ns = list(map(int, input().split()))
  ms = list(map(int, input().split()))
  res = 0
  mx = 0
  for num1 in ns:
    num_to_remove = 0
    r = False
    for num in ms:
      print(num, num1)
      if abs(num - num1) > mx:
        mx = abs(num - num1)
        r = True
        num_to_remove = num
    res += mx
    if r:
      ms.remove(num_to_remove)
      r = False
    
  print(mx)
    
# 3 5
# 6 5 2
# 1 7 9 7 2