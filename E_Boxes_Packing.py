n = int(input())
boxes = list(map(int,input().split()))
counter = {}
for box in boxes:
  if box in counter:
    counter[box] += 1
  else:
    counter[box] = 1
print(max(counter.values()))

   
  