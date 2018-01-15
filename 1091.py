


while(True):
  
  
  K = int(input())
  if K == 0:
    break
  N, M = [int(i) for i in input().split(' ')]
  
  
  for i in range(K):
    X, Y = [int(i) for i in input().split(' ')]
    if X == N or Y == M:
      print('divisa')
    elif X > N and Y > M:
      print('NE')
    elif X > N and Y < M:
      print('SE')
    elif X < N and Y > M:
      print('NO')
    elif X < N and Y < M:
      print('SO')
      
  
  
  

