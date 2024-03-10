p = list(map(int, input().split()))
m = list(map(int, input().split()))
w = 0
l = 0
for i in range(len(p)):
  if i <= 2:
    w += (p[i] * m[i])
  else:
    l += (p[i] * m[i])
if w > l:
  print("WIN")
elif l > w:
  print('LOSE')
else:
  print('DRAW')
