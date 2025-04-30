def converter(str):
    binaryStr = ''
    for i in range(len(str)):
        unicode = ord(str[i])
        if unicode < 128:
            binary_char = bin(unicode)[2:]
            while len(binary_char) < 8:
                binary_char = '0' + binary_char
        binaryStr += binary_char
    return binaryStr

def deconverter(binaryStr):
    str = ''
    sizeOfChar = 8
    arrBin = [binaryStr[i:i+sizeOfChar] for i in range(0, len(binaryStr), sizeOfChar)]
    for j in range(len(arrBin)):
        inteiro = int(arrBin[j], 2)
        str += chr(inteiro)
    return str


#def main():
#    print(deconverter(converter("Hello")))

#main()