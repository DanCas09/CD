from bsc import BSC
from interleaving import interleaving, deinterleaving

#def bits_to_string(bits):
    # Join the list of bits into a single string
#    bit_string = ''.join(map(str, bits))

    # Split the bit string into chunks of 8 bits
#    chunked_bits = [bit_string[i:i+8] for i in range(0, len(bit_string), 8)]

    # Convert each 8-bit chunk to its corresponding ASCII character
#    characters = [chr(int(chunk, 2)) for chunk in chunked_bits]

    # Join the list of characters into a single string
#    return ''.join(characters)

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


def main():
    # Message to be transmitted
    TX = "Bom dia, esta tudo bem consigo?!"

    # Interleaving matrix size
    c = 4
    l = 8

    # Apply interleaving to the message
    matrix = interleaving(TX, c, l)
    print("Interleaving matrix:")
    for row in matrix:
        print(row)

    # Convert the message to a sequence of bits
    bits = matrix_to_binary(matrix)
   
    # Apply binary symmetric channel with desired BER
    BER = 0.00390625
    new_bits = BSC(bits, BER)

    # Convert the received bits back to the matrix of ASCII characters
    new_matrix = binary_to_matrix(new_bits, c, l)
    print("\nDeinterleaving matrix:")
    for row in new_matrix:
        print(row)

    # Deinterleave the received message
    RX = deinterleaving(new_matrix)

    print("\nTransmitted message: ", TX)
    print("Received message: ", RX)
    print("Transmitted message (bits): ", array_to_string(bits))
    print("Received message (bits): ", new_bits)

    # Calculate the actual  BER
    errors = sum([1 for i in range(len(new_bits)) if array_to_string(bits)[i] != new_bits[i]])
    BER_real = errors / len(new_bits)
    print("\nDesired BER: ", BER)
    print("Actual BER:  ", BER_real)

if __name__ == '__main__':
    main()
