n = int(input())
nums  = [int(num) for num in input().split()]
count = 0
nums.sort()
counter = {}
c = True
for num in nums:
  if num in counter:
    counter[num] += 1
  else:
    counter[num] = 1
while c:
  for key in counter:
    if counter[key] > 0:
      counter[key] -= 1
      
  count += 1
  lists = [counter[key] for key in counter]
  if set(lists) == set([0]):
    c = False
print(count)
      
  