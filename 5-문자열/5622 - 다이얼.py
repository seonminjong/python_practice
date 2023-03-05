l = ['A,B,C','D,E,F','G,H,I','G,K,L','M,N,O','P,Q,R,S','TUV','WXYZ']
a = input() #WK 
reset = 0
for i in range(len(a)): #2번
  for j in l:
    if a[i] in j:
      reset += l.index(j) + 3
print(reset)
