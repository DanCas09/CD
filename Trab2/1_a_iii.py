from Converters import converter
from Converters import deconverter
from Hamming74 import codHamming74
from Hamming74 import decodHamming74
from bsc import BSC

def readFile(f):
    with open(f,'r') as f:
        a = f.read().replace('\n','')
    return a

def main():
    bers = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    files = ['./testFiles/a.txt', './testFiles/Person.java', './testFiles/progc.c', './testFiles/alice29.txt']
    for j in range(len(files)):
        print(files[j])
        A = readFile(files[j])
        for i in range(len(bers)):
            print("-----------------------------------------------------------------------")
            bin_sqc = converter(A)
            print(f"Número de caracteres:{len(A)}")

            H74 = codHamming74(bin_sqc) 
    
            initialBer1 = bers[i]
            bsc_sqc = BSC(H74, initialBer1)

            errors1 = sum([1 for i in range(len(bsc_sqc)) if bsc_sqc[i] != H74[i]])
            print(f"Número de bits trocados:{errors1}")
            BER1 = errors1 / len(bsc_sqc)
            print("\nDesired BER1: ", initialBer1)
            print("Actual BER1:  ", BER1)
    
            H47 = decodHamming74(bsc_sqc)

            errors2 = sum([1 for i in range(len(bin_sqc)) if bin_sqc[i] != H47[i]])
            BER2 = errors2 / len(bin_sqc)
            print("\nDesired BER2: ", 0)
            print("Actual BER2: ", BER2)

            B = deconverter(H47)
            print("Nº total de bits que passam no BSC: ", len(H74))
            difChars = sum([1 for i in range(len(A)) if A[i] != B[i]])
            print("Nº de símbolos diferentes entre A e B:", difChars)


main()