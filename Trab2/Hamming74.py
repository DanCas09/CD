def table(sindroma):
    if(sindroma == '000'):
        return '0000000' #Ausência de erro
    if(sindroma == '011'):
        return '1000000' #1.º bit em erro
    if(sindroma == '110'):
        return '0100000' #2.º bit em erro
    if(sindroma == '101'):
        return '0010000' #3.º bit em erro
    if(sindroma == '111'):
        return '0001000' #4.º bit em erro
    if(sindroma == '100'):
        return '0000100' #5.º bit em erro
    if(sindroma == '010'):
        return '0000010' #6.º bit em erro
    if(sindroma == '001'):
        return '0000001' #7.º bit em erro

def getb0(str):
    m1 = int(str[1])
    m2 = int(str[2])
    m3 = int(str[3])
    return m1 ^ m2 ^ m3

def getb1(str):
    m0 = int(str[0])
    m1 = int(str[1])
    m3 = int(str[3])
    return m0 ^ m1 ^ m3

def getb2(str):
    m0 = int(str[0])
    m2 = int(str[2])
    m3 = int(str[3])
    return m0 ^ m2 ^ m3

def XORBitaBit(transmittedParity, expectedParity):
    if(len(transmittedParity) != len(expectedParity)):
        print("tamanho diferente")
        return 
    xor = ''
    for i in range(len(transmittedParity)):
        temp = int(transmittedParity[i]) ^ int(expectedParity[i])
        xor += f'{temp}'
    return xor

def codHamming74(str):
    res = ''
    curr = ''
    for i in range(len(str)):
        curr += str[i]
        if (len(curr) == 4):
            b0 = getb0(curr)
            b1 = getb1(curr)
            b2 = getb2(curr)
            res += (curr + f'{b0}' + f'{b1}' + f'{b2}')
            curr = ''
    return res

def decodHamming74(str,): # k => bits de entrada , n => bits de saída
    res = ''
    curr = ''
    expectedParity = ''
    for i in range(len(str)):
        curr += str[i]
        if(len(curr) == 4): #if(len(curr) == k):
            expectedb0 = getb0(curr)
            expectedb1 = getb1(curr)
            expectedb2 = getb2(curr)
            expectedParity = f'{expectedb0}' + f'{expectedb1}' + f'{expectedb2}'
        if(len(curr) == 7): #if(len(curr) == n):  
            sindroma = XORBitaBit(curr[4:7], expectedParity) # XORBitaBit(curr[k:n], expectedParity)
            error = table(sindroma)
            res += XORBitaBit(curr[0:4],error[0:4]) # XORBitaBit(curr[0:k],error[0:k])
            curr = ''
    return res

#def main():
#    print(codHamming74("11001100"))  
#    print(decodHamming74("11001011100101"))

#main()