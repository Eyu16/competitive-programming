import sys
n = int(input())
nums =  list(map(int,input().split()))
changed = False
x = 1
y = 1
for i in range(len(nums) - 1):
  if nums[i] < nums[i + 1]:
    continue
  if changed:
    print('no')
    sys.exit()
  if i == 0 or nums[i + 1] > nums[i-1]:
    nums[i] = nums[i - 1]
    x = i
    y = i - 1
    changed = True
  else:
    nums[i + 1] = nums[i]
    x = i
    y = i + 1
print('yes')
print(x, y)

    
    