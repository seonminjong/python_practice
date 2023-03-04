n = int(input())
l = list(map(int,input().split()))

m = max(l)

a = sum(l) / m * 100 / n
print(a)