r1 = [char for char in input()]
r2 = [char for char in input()]
r3 = [char for char in input()]
pair_win = 0
ind_win = 0
if len(set(r1)) == 2:
  pair_win += 1 
elif len(set(r1)) == 1:
  ind_win += 1
if len(set(r2)) == 2:
  pair_win += 1 
elif len(set(r2)) == 1:
  ind_win += 1
if len(set(r3)) == 2:
  pair_win += 1 
elif len(set(r3)) == 1:
  ind_win += 1
s1 = set([r1[0],r2[0],r3[0]])
s2 = set([r1[1],r2[1],r3[1]])
s3 = set([r1[2],r2[2],r3[2]])
s4 = set([r1[0],r2[1],r3[2]])
s5 = set([r1[2],r2[1],r3[0]])

if len(s1) == 2:
  pair_win += 1
elif len(s1) ==  1:
  ind_win += 1
  
if len(s2) == 2:
  pair_win += 1
elif len(s2) ==  1:
  ind_win += 1
  
  
if len(s3) == 2:
  pair_win += 1 
elif len(s3) ==  1:
  ind_win += 1
  
if len(s4) == 2:
  pair_win += 1 
elif len(s4) ==  1:
  ind_win += 1
  
  
if len(s5) == 2:
  pair_win += 1 
elif len(s5) ==  1:
  ind_win += 1
  
print(ind_win)
print(pair_win)
   