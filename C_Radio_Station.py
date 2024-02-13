n, m = map(int, input().split())
maped = {}
for i in range(n):
  list = input().split()
  maped[list[1]]= list[0]
for i in range(m):
  list = input().split()
  ip = list[1][:-1]
  print(f"{list[0]} {list[1]} #{maped[ip]}")
  
