size, n = map(int, input().split())

l = [0 for i in range(size)]
#[i for i in range(size)]면 
#0 1 2 3 4 5 로 출력
for _ in range(n):
  left, right, ball = map(int, input().split())
  l[left - 1:right] = [ball] * (right - left + 1)# = 앞이랑 같게 해준다

print(*l)


