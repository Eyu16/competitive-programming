s = input()  
consequitve_fours = set()
counter = 0
for i in range(len(s)):
  if s[i] == '4':
    counter += 1
  else:
    consequitve_fours.add(counter)
    counter = 0
else:
  consequitve_fours.add(counter)

if consequitve_fours <= set([0,1,2])  and s[0] == '1' and set(s) <= set(['1','4']):
  print('YES')
else:
  print('NO')
    
  
      
  