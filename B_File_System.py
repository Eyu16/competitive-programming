from collections import defaultdict
n = int(input())
fr =  defaultdict(int)
for i in range(n):
  name = input()
  if fr[name] == 0:
    print('OK')
    fr[name] += 1
  else:
    print(name + str(fr[name]))
    fr[name] += 1
    
  