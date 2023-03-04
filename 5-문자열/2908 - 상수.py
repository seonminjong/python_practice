a, b = input().split()  #int는 뒤집을 수 없음
a = int(a[::-1])
b = int(b[::-1])

if a > b:
  print(a)
else:
  print(b)
