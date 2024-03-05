n = int(input())
nums = list(map(int, input().split()))
negatives = []
positives = []
zeros = []
negative_notfound = True
counts = 0
for num in nums:
  if num < 0:
    counts += 1
    
if counts % 2 == 0:
  first = True
  second = True
  for num in nums:
    if num < 0:
      if first:
        negatives.append(num)
        first = False
      elif second:
        zeros.append(num)
        second = False
      else:
        positives.append(num)   
    elif num > 0:
      positives.append(num)
    else:
      zeros.append(num)
else:
  first = True
  for num in nums:
    if num < 0:
      if first:
        negatives.append(num)
        first = False
      else:
        positives.append(num)
    elif num > 0:
      positives.append(num)
    else:
      zeros.append(num)
      
print(len(negatives)," ".join(list(map(str,sorted(negatives)))))
print(len(positives), " ".join(list(map(str,sorted(positives)))))
print(len(zeros), " ".join(list(map(str,sorted(zeros)))))

  