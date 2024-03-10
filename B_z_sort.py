n = int(input())
nums = input().split()
nums.sort()
if len(nums) < 3:
  print(" ".join(nums))
else:
  res = [nums[0]]
  i = 1
  j = len(nums) - 1
  while i <= j:
    if i == j:
      res.append(nums[j])
    else:
      res.append(nums[j])
      res.append(nums[i])
    i += 1
    j -= 1
  e_s = True
  for i in range(1, len(res) - 1, 2):
    if res[i] < res[i - 1]:
      e_s =  False
      break
    
  if e_s:
    print(" ".join(res))
  else:
    print('Impossible')
  
  