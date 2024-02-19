n = int(input())
nums = input().split()
m = int(input())
queries = input().split()
d = {}
v_count = 0
p_count = 0
for i, num in enumerate(nums):
  d[num] = i
for query in queries:
  index = d[query]
  v_count += abs(index + 1)
  p_count += abs(n - index)
      
print(v_count, p_count)
  
  