n = str(input())
a = 'abcdefghijklmnopqrstuvwxyz'
#alphabet_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in a:
  if i in n:
    print(n.index(i),end =' ')
  else:
    print(-1,end =' ')

'''a = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(a.find(x), end = ' ')'''