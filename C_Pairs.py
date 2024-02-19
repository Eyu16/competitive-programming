from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a_f = Counter(a)
count = 0
for i in range(n):
  j = c[i] - 1
  if b[j] in a_f:
    count += a_f[b[j]]
print(count)
    
