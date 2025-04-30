from Converters import converter
from Converters import deconverter
from R31 import cod
from R31 import decod
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

            initialBer1 = bers[i]
            bsc_sqc = BSC(bin_sqc, initialBer1)

            errors1 = sum([1 for i in range(len(bsc_sqc)) if bin_sqc[i] != bsc_sqc[i]])
            print(f"Número de bits trocados:{errors1}")
            BER1 = errors1 / len(bsc_sqc)
            print("\nDesired BER1: ", initialBer1)
            print("Actual BER1:  ", BER1)
    
            B = deconverter(bsc_sqc)
            print("Nº total de bits que passam no BSC: ", len(bsc_sqc))
            difChars = sum([1 for i in range(len(A)) if A[i] != B[i]])
            print("Nº de símbolos diferentes entre A e B:", difChars)

        
main()