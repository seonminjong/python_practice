size, n = map(int, input().split())

l = [0 for i in range(size)]

for _ in range(n):
  left, right, ball = map(int, input().split())
  l[left - 1:right] = [ball] * (right - left + 1)

print(*l)


