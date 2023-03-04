n, x = map(int, input().split())
l = list(map(int, input().split()))
print(*[i for i in l if i < x])

# for i in list:
#   if i < x:
#     print(i, end=' ')
