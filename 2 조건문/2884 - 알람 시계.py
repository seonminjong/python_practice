H, M = map(int, input().split())
if H > 24 or M > 59 or H < 0 or M < 0:
  print("시계에 그런 수는 없습니다")
elif M > 45:
  print(H, M-45)
elif M < 45 and H > 0:
  print(H-1, M+15)
else:
  print(23, M+15)