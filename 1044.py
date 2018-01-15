
x, y =  [int(i) for i in input().split()]

if x== 0 or y==0:
  print('Sao Multiplos')
elif (y%x==0 or x%y ==0):
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')