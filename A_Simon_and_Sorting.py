t =  int(input())

for _ in range(t):
  word  = input()
  if 0 == word.index('a') or 1 == word.index('b') or 2 == word.index('c'):
    print('YES')
  else:
    print('NO')
  