a = input().upper()
l = [0 for i in range(26)]

for char in a:
  l[ord(char)-65] += 1


if l.count(max(l)) > 1:
  print("?")
else:
  print(chr(l.index(max(l)) + 65))