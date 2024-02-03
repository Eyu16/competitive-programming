test_case = int(input())
for _ in range(test_case):
  length = int(input())
  order = input()
  counter = {}
  for letter in order:
    if letter in counter:
      counter[letter] += 1
    else:
      counter[letter] = 1
  count = 0
  for key in counter:
    if counter[key] >= 2:
      count += (2 + counter[key] - 1)
    else:
      count += 2
  print(count)
    

  # print(count_A * 2 + length)





