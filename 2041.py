
def get_nextSequence(s):

    s.append('0') # marcando o fim da string
    string = []
    cont = 1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            cont = cont + 1
        else:
            string.append(cont)
            string.append(s[i])
            cont = 1
    nextSequence = ''.join(map(str, string))
    return nextSequence

N = -1
while(True):
    try:
        N = int(input())
        sequence = '3'

        for j in range(N-1):
            if N == 1:
                print(sequence)
            else: 
                aux = []
                aux = get_nextSequence(list(sequence))
                sequence = aux[:]
        print(sequence)
    except EOFError:
        break
        
    