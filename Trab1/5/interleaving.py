def interleaving(msg, c, l):
    matrix = [[''] * c for i in range(l)]
    index = 0  
    for i in range(l):
        for j in range(c):
            if index >= len(msg):
                break
            matrix[i][j] = msg[index]
            index += 1   
    return matrix


def deinterleaving(matrix):
    l = len(matrix)
    c = len(matrix[0])
    sequence = ''
    
    for i in range(l):
        for j in range(c):
            if matrix[i][j] != '':
                sequence += matrix[i][j]
    
    return sequence

#def main():
#    msg = "ExemploDeTransmissaoInterleaving"
#    nrCollumns = 4 
#    nrLines = 8
#    matrix = interleaving(msg, nrCollumns, nrLines)
#    print(matrix)
#    print(deinterleaving(matrix))

#main()