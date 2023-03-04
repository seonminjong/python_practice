x = int(input())  # 5000
n = int(input())  # 5
sum = 0
for i in range(n):
  a, b = map(int, input().split())
  sum += a * b
if sum == x:
  print("true")
else:
  print("fuck you")
