

Q, E = [int(i) for i in input().split()]

SI = [int(j) for j in input().split()]

for z in range(Q):
    CI = int(input())
    if CI in SI:
        print ('0')
    else:
        print('1')
        SI.append(CI)
        
