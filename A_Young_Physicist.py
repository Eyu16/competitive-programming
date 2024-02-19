n = int(input())
xs =  []
ys = []
zs = []
for _ in range(n):
  x,y,z = map(int, input().split())
  xs.append(x)
  ys.append(y)
  zs.append(z)
  
if sum(xs) == 0 and sum(ys) == 0 and sum(zs) == 0:
  print("YES")
else:
  print( "NO")
  


  
  


  