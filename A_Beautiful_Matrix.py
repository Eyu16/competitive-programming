i = 0
j = 0
for k in range(5):
  row = input().split()
  if '1' in row:
    j = row.index('1')
    i = k
    break
  i = k
moves = abs(2 - i) + abs(2 - j)
print(moves)

