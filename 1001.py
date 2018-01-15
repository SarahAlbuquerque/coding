
value = int(input())

def quantidade_de_notas (nota, value):
    return int(value/nota)

notas = [1, 2, 5, 10, 20, 50, 100]
for i in notas:
    quantidade_de_notas(i,)

    

n_100 = int(value/100)
n_50 = int((value - n_100*100)/50)
n_20 = int((value - n_100*100 - n_50 * 50)/20)
n_10 = int((value - n_100*100 - n_50 * 50 - n_20 * 20)/10)
aux = value - n_100*100 - n_50 * 50 - n_20 * 20 - n_10 * 10
n_5 = int((aux)/5)
n_2 = int((aux-n_5*5)/2)
n_1 = int((aux-n_5*5-n_2*2))

print(value)
print('{:d} nota(s) de R$ 100,00'.format(n_100))
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00

