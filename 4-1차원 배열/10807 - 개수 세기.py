n = int(input())
n_list = list(map(int, input().split()))
a = int(input())
if len(n_list) == n:
  print(n_list.count(a))
