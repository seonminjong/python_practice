l = list(range(1, 31))

for _ in range(28):
  inp = int(input())
  l.remove(inp)
for i in l:
  print(i)