N = int(input())




banknotes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00]

print(N)
for i in banknotes:
  number_notes = int(N/i)
  string = '{:d} nota(s) de R$ {:.2f}'.format(number_notes, i)
  print(string.replace('.', ','))
  N = N - number_notes * i
  