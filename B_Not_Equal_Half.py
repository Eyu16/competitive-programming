n = int(input())
nums = list(map(int,input().split()))
if len(set(nums) ) == 1:
  print('-1')
else:
  nums.sort()
  print(" ".join(map(str,nums)))
