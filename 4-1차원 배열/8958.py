n = int(input())

for i in range(n):
  l = input()
  r = 0
  q = 0
  for e in l:
    if e == 'O':
      r += 1  # 1
      q += r  # 1
    else:
      r = 0
  print(q)

# n = int(input())

# for _ in range(n):
#   inp = input().split("X")
#   print(inp)
#   score = 0
#   for a in inp:
#     if (j := len(a)) > 0:
#       score += (j * (j + 1)) // 2
#   print(score)
