t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int,input().split()))
  a.sort()
  diff = float('inf')
  for i in range(len(a) - 1):
    diff = min(diff, a[i + 1] - a[i])
  print(diff)