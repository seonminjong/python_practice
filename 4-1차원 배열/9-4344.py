n = int(input())
for i in range(n):
  a = list(map(int, input().split()))
  p = sum(a[1:]) / a[0]
  cut = 0

  for r in a[1:]:
    if r > p:
      cut += 1

  print(f"{cut / a[0] * 100:.3f}%")


# n = int(input())
# for _ in range(n):
#     l = list(map(int, input().split()))
#     print(f"{len([i for i in l[1:] if i > (sum(l[1:]) / l[0])]) / l[0] * 100:.3f}%")



