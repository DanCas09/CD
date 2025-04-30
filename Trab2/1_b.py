from Converters import converter
from Converters import deconverter
from R31 import cod
from R31 import decod
from bsc import BSC
from interleaving import interleaving
from interleaving import deinterleaving
from interleaving import binary_to_matrix
from interleaving import matrix_to_binary
from interleaving import array_to_string
from Hamming74 import codHamming74
from Hamming74 import decodHamming74

def r31():
    bers = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    TX = 'Hello, how are you?are you good?'
    c = 4
    l = 8
    for i in range(len(bers)):
        A = interleaving(TX, c, l)
    
        bin_sqc = array_to_string(matrix_to_binary(A))

        R31 = cod(bin_sqc)
   
        initialBer1 = bers[i]
        bsc_sqc = BSC(R31, initialBer1)

        errors1 = sum([1 for i in range(len(bsc_sqc)) if bsc_sqc[i] != R31[i]])
        BER1 = errors1 / len(bsc_sqc)
        print("\nDesired BER1: ", initialBer1)
        print("Actual BER1:  ", BER1)
    
        R13 = decod(bsc_sqc)

        errors2 = sum([1 for i in range(len(bin_sqc)) if bin_sqc[i] != R13[i]])
        BER2 = errors2 / len(bin_sqc)
        print("\nDesired BER2: ", 0)
        print("Actual BER2: ", BER2)

        B = binary_to_matrix(R13, c , l)

        RX = deinterleaving(B)
        print(RX)
        print("Nº total de bits que passam no BSC: ", len(R31)) # 768
        difChars = sum([1 for i in range(len(TX)) if TX[i] != RX[i]])
        print("Nº de símbolos diferentes entre A e B:", difChars)
        print("-----------------------------------------------------------------------")

        
def hamming():
    bers = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    TX = 'Hello, how are you?are you good?'
    c = 4
    l = 8
    for i in range(len(bers)):
        A = interleaving(TX, c, l)

        bin_sqc = array_to_string(matrix_to_binary(A))

        H74 = codHamming74(bin_sqc) 
   
        initialBer1 = bers[i]
        bsc_sqc = BSC(H74, initialBer1)

        errors1 = sum([1 for i in range(len(bsc_sqc)) if bsc_sqc[i] != H74[i]])
        BER1 = errors1 / len(bsc_sqc)
        print("\nDesired BER1: ", initialBer1)
        print("Actual BER1:  ", BER1)
    
        H47 = decodHamming74(bsc_sqc)

        errors2 = sum([1 for i in range(len(bin_sqc)) if bin_sqc[i] != H47[i]])
        BER2 = errors2 / len(bin_sqc)
        print("\nDesired BER2: ", 0)
        print("Actual BER2: ", BER2)

        
        B = binary_to_matrix(H47, c , l)

        RX = deinterleaving(B)
        print(RX)
        print("Nº total de bits que passam no BSC: ", len(H74)) # 448
        difChars = sum([1 for i in range(len(TX)) if TX[i] != RX[i]])
        print("Nº de símbolos diferentes entre A e B:", difChars)
        print("-----------------------------------------------------------------------")

print("----------------------------Repetição (3,1)----------------------------")
r31()
print("-----------------------------Hamming (7,4)-----------------------------")
hamming()