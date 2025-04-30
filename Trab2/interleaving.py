def array_to_string(bits):
    string = ''
    for i in range(0, len(bits)):
        string += str(bits[i])
    return string


def binary_to_matrix(bits, c, l):
    # Converts a list of bits to chars into a matrix of size c x l
    matrix = [[''] * c for i in range(l)]
    index = 0
    sizeOfChar = 8
    arrBin = [bits[i:i+sizeOfChar] for i in range(0, len(bits), sizeOfChar)]
    for i in range(l):
        for j in range(c):
            if index <= 31:
                inteiro = int(arrBin[index], 2)
                matrix[i][j] = chr(inteiro)
                index += 1
    return matrix


def matrix_to_binary(matrix):
    # Converts a matrix of ASCII characters into a list of bits
    bits = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            unicode = ord(matrix[i][j])
            # Handle ASCII control characters
            if unicode < 128:
                binary_char = bin(unicode)[2:]
                while len(binary_char) < 8:
                    binary_char = '0' + binary_char
                for k in range(8):
                    bits.append(int(binary_char[k]))
    return bits


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