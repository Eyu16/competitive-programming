n = int(input())
num_dic = {}
nums = list(map(int, input().split()))
for i in range(len(nums) - 1):
  min_idex = i
  for j in range(i + 1, len(nums)):
    if nums[min_idex] > nums[j]:
      min_idex = j
  nums[i], nums[min_idex] = nums[min_idex], nums[i]
  if min_idex != i:
    num_dic[i] = [f"{i}", f"{min_idex}"] 
print(len(num_dic))

for key in num_dic:
  print(" ".join(num_dic[key]))
  