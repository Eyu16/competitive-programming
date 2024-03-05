# from collections import defaultdict
# n, m = map(int, input().split())
# difficulties = list(input().split())
# dicti = defaultdict(int)
# count = 0
# for diff in difficulties:
#   if dicti[diff] == 0:
#     count += 1
#     if count == n:
#       print('1',end='')
#       count = 0
#       for key in dicti:
#         if dicti[key] - 1 > 0:
#           count += 1
#         if dicti[key] > 0:
#           dicti[key] -= 1
#     else:
#       print('0',end='')
#       dicti[diff] = 1
#   else:
#     print('0',end='')
#     dicti[diff] += 1



n, m = map(int,input().split())
a = list(map(int,input().split()))
md = {}
ans =[]
ml = 0
for i in a:
    ml += md.get(i,0) ==0
    md[i] = md.get(i,0) + 1
    if  ml==n:
        ans.append('1')
        for i in list(md):
            md[i]-=1
            if not md[i]:
                ml-=1
    else:
        ans.append('0')
print("".join(ans))

