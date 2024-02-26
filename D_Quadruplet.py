import sys
n, target = map(int,input().split())
nums = list(map(int,input().split()))
sum_dict = {}
sum_set = set()
for i in range(len(nums)):
  for j in range(i+1, len(nums)):
      sum = nums[i] + nums[j]
      if target - sum in sum_dict:
        sum_set.update([sum_dict[target-sum][0],sum_dict[target-sum][1],i+1,j+1])
        if len(sum_set) == 4:
          l = sorted(list(sum_set))
          print(l[0],l[1],l[2],l[3])
          sys.exit()
        sum_set = set()
      else:
        sum_dict[sum] = (i+1,j+1)
        
print('IMPOSSIBLE') 

