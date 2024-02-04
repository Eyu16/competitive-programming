# test_case = int(input())
# for _ in range(test_case):
#   numString = int(input())
#   strings  = []
#   stringSums = set()
#   final_result = ""
  
#   for _ in range(numString):
#     new_string = input()
#     strings.append(new_string)
    
#   for string in strings:
#     found = False
#     for i in range(len(string)):
#       prefix = string[i + 1:]
#       suffix = string[:i + 1]
#       if prefix in strings and  suffix in strings:
#         found = True
#         break
#     if found:
#       final_result += '1'
#     else:
#       final_result += '0'
#   print(final_result)
        
tests = int(input())

for _ in range(tests):
    NumOfStrings = int(input())

    phrases = {}
    words = []

    for _ in range(NumOfStrings):
        temp = input().strip()
        phrases[temp] = False
        words.append(temp)

    for k in range(NumOfStrings):
        current_word = words[k]
        length = len(current_word)

        for o in range(length):
            partition1 = current_word[:o + 1]
            partition2 = current_word[o + 1:]

            if partition1 in phrases and partition2 in phrases:
                phrases[current_word] = True

    result = ''.join(['1' if phrases[word] else '0' for word in words])
    print(result)

        
      
  
  
    


      
        
        
      
   
    
 