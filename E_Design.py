n, q = map(int, input().split())
words = input().split()
for _ in range(q):
  p, s = input().split()
  for i, word in enumerate(words):
    if p in word:
      p_i = word.index(p)
    else:
      p_i = -1
    if s[::-1] in word[::-1]:
      s_i = word[::-1].index(s[::-1])
    else:
      s_i = -1
    if p_i == 0 and s_i == 0:
      print(i)
      break
  
