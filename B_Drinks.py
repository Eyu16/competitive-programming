n = int(input())
l = input().split()
sum = 0
for num in l:
  sum += int(num)
r = round(sum/n,12)
formatted_number = "{:.12f}".format(r)
print(formatted_number)

  
# print(len('66.6666666666667'))
