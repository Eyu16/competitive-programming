from collections import Counter
s = input()
map_fr = Counter(s)
odd_count = 0
for key in map_fr:
  if map_fr[key] % 2 != 0:
    odd_count += 1
    
if odd_count == 0 or (odd_count - 1) % 2 == 0:
  print('First')
else:
  print('Second')