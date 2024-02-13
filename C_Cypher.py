test_case = int(input())
for _ in range(test_case):
  n = int(input())
  current_code = input().split() 
  moves_made = []
  initial_code = []
  for _ in range(n):
    new_move = input().split()[1]
    moves_made.append(new_move)
  for i in range(n):
    code = int(current_code[i])
    move_made = moves_made[i]
    count_d = move_made.count('D')
    count_u = move_made.count('U')
    move = count_d - count_u
    if move > 0:
      for _ in range(abs(move)):
        if code + 1 == 10:
          code = 0
        else:
          code += 1
    elif move < 0:
      for _ in range(abs(move)):
        if code - 1 == -1:
          code = 9
        else:
          code -= 1
          
    initial_code.append(code)
    result = ' '.join(map(str,initial_code))
  print(result)
  
      
          
        
        
        
      
        
      
    
    
    
  

  # data = input().split()
  # print(data)
#
