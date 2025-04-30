import random

def BSC(bits, BER):
    copy = list(map(int, bits))
    for i in range(len(copy)):
        if random.random() < BER:
            copy[i] = 1 - copy[i]
    return ''.join(map(str, copy))



#def main():
#    b = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
#    initialBer = 0.01 # 10
#    bsc = BSC(b,initialBer)
#    nrOfZeros = bsc.count("0") 
#    newBer = nrOfZeros / len(b)
#    print(newBer)
    
#main()