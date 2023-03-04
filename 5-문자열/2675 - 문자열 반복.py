n = int(input())

for _ in range(n):
  num, word = input().split()
  num = int(num)
  s = ""
  for char in word:
    s += char * num
  print(s)
