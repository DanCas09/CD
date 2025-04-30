import random

# def BSC(binarySequence, Ber):
#     decimal = numberOfDecimal(Ber) # número de casas decimais
#     copy = binarySequence
#     for i in range(0, len(copy)):
#         if(random.randint(0, pow(10,decimal) - 1) <= Ber * pow(10,decimal) - 1):
#             copy[i] = ~copy[i] & 1
#     return copy

# def numberOfDecimal(Ber):
#     return len(str(Ber)) - str(Ber).index('.') - 1

def BSC(bits, BER):
    copy = list(map(int, bits))
    print(copy)
    for i in range(len(copy)):
        if random.random() < BER:
            copy[i] = 1 - copy[i]
    return ''.join(map(str, copy))



def main():
    b = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    initialBer = 0.01 # 10
    bsc = BSC(b,initialBer)
    nrOfZeros = bsc.count("0") 
    newBer = nrOfZeros / len(b)
    print(newBer)
    
main()