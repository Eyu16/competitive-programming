n = int(input())
capacities = []
sums = 0
for _ in range(n):
  outs, ins = map(int,input().split())
  sums += (ins - outs)
  capacities.append(sums)
  
print(max(capacities))
  

  