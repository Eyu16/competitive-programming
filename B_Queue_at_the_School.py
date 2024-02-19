n, t = map(int, input().split())
que = list(input())
for _ in range(t):
  i = 0
  j = 1
  while i < n and j < n:
    if que[i] == 'B' and que[j] == 'G':
      que[i], que[j] = que[j], que[i]
      i += 2
      j += 2
    else:
      i += 1
      j += 1
print("".join(que))
    
  