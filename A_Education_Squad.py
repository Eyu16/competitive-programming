matrix = [[char for char in input()],
[char for char in input()],
[char for char in input()]]



indivisual_win = set()
group_win = set()


def winner(row):
  s = set(row)
  if len(s) == 1:
    s = sorted(list(s))
    s = "".join(s)
    indivisual_win.add("".join(list(s)))
  elif len(s) == 2:
    s = sorted(list(s))
    s = "".join(s)
    group_win.add(s)
    
    
for i in range(3):
  winner(matrix[i])
  
  s = []
  
  for j in range(3):
    s.append(matrix[j][i])
  winner(s)
  


winner([matrix[0][2], matrix[1][1], matrix[2][0]])
winner([matrix[0][0], matrix[1][1], matrix[2][2]])

print(len(indivisual_win))
print(len(group_win))



    
    
    

  
    
  
  
  





# pair_win = 0
# ind_win = 0
# if len(set(r1)) == 2:
#   pair_win += 1 
# elif len(set(r1)) == 1:
#   ind_win += 1
# if len(set(r2)) == 2:
#   pair_win += 1 
# elif len(set(r2)) == 1:
#   ind_win += 1
# if len(set(r3)) == 2:
#   pair_win += 1 
# elif len(set(r3)) == 1:
#   ind_win += 1
# s1 = set([r1[0],r2[0],r3[0]])
# s2 = set([r1[1],r2[1],r3[1]])
# s3 = set([r1[2],r2[2],r3[2]])
# s4 = set([r1[0],r2[1],r3[2]])
# s5 = set([r1[2],r2[1],r3[0]])

# if len(s1) == 2:
#   pair_win += 1
# elif len(s1) ==  1:
#   ind_win += 1
  
# if len(s2) == 2:
#   pair_win += 1
# elif len(s2) ==  1:
#   ind_win += 1
  
  
# if len(s3) == 2:
#   pair_win += 1 
# elif len(s3) ==  1:
#   ind_win += 1
  
# if len(s4) == 2:
#   pair_win += 1 
# elif len(s4) ==  1:
#   ind_win += 1
  
  
# if len(s5) == 2:
#   pair_win += 1 
# elif len(s5) ==  1:
#   ind_win += 1
  
# print(ind_win)
# print(pair_win)
