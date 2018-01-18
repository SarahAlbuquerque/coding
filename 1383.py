
def get_values(n_rows):
    values = []
    for i in range(n_rows):
        values.append([int(j) for j in input().split()])
    return values

def get_arrays(v, n):
    div = len(v)/n #nesse caso sempre 9
    
    arrays = []
    range_list = []
    il = 0
    sl = 0
    for k in range(n):
        sl = sl + int(div)
        range_list.append(range(il,sl))
        il = sl
    for i in range_list:
        aux_array= []
        for j in i:
            aux_array.append(v[j])
        arrays.append(aux_array)
    return arrays


def check_row(array):
    result = True
    for i in array:
       result = result and areThereAllAlgorisms(i)
    return result

def get_smaller_arrays(array):
    range_list = []
    il = 0 # limite nferior
    sl = 0 # limite superior
    for k in range(int(pow(len(array), 1/2))):
        sl = sl + int(pow(len(array), 1/2)) 
        range_list.append(range(il,sl))
        il = sl
    smallers_arrrays = []
    for a in range_list:
        for b in range_list:
            aux_arrray = []
            for i in a:
                for j in b:
                    aux_arrray.append(array[i][j])
            smallers_arrrays.append(aux_arrray)
    return smallers_arrrays   

def get_columns(array):
    t_array = []
    for j in range(len(array)):
        column = []
        for i in range (len(array)):
            column.append(array[i][j])
        t_array.append(column)
    return t_array 


def areThereAllAlgorisms (row):
  vetorConfere = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  return bool(sorted(row)==vetorConfere)



n = int(input())
a = get_values(9*n)
n_arrays = get_arrays(a, n)

inst = 1
for i in n_arrays:
    
    # verificar linha por linha
    row_result = check_row(i)
    
    # verificar matriz menores por matrizes menores
    b = get_smaller_arrays(i)
    array_result = check_row(b)

    # verificar as colunas
    c = get_columns(i)
    columns_result = check_row(c)
    
    result = row_result and array_result and columns_result
    
    print('Instancia {:d}'.format(inst))
    inst = inst + 1

    if(result):
        print('SIM\n')
    else:
        print('NAO\n')
    
  
