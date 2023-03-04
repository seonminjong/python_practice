a, b, c = map(int, input().split())
A = int
if a == b == c:
    A = 10000 + a*1000
    print(A)
elif a == c:
  print(1000+a*100)
  if a == b:
     print(1000+a*100)
  if c == b:
     print(100+c*100)
elif a != b != c:
    print(100*max(a,b,c))
        