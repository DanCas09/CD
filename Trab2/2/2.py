import serial
import time
import random
import struct
import FletcherChecksumLib

arr = [2, 3, 4.5, 6.75, 10.13, 15.19, 22.78, 34.17, 51.26, 76.87]
for i in range(len(arr)):
    print(arr[i])

def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))

def xor(value1, value2):
    value1Binary = binary(value1)
    value2Binary = binary(value2)
    result = ""
    for char1, char2 in zip(value1Binary, value2Binary):
        xor_result = str(int(char1) ^ int(char2))
        result += xor_result
    print("Valor do termo                       Valor do Erro                       Result")    
    print(value1Binary,"xor" ,value2Binary, '->', result)
    print("Before Error(float):", value1)
    print("After error(float):", BinaryToFloat(result))

    return result

def BinaryToFloat(value):
    binaryRes = int(value, 2).to_bytes(4, 'big')
    return struct.unpack('!f', binaryRes)[0]

def generateError():
    position = random.randint(0, 31)
    
    binary_string = '0' * 32
   
    binary_string = binary_string[:position] + '1' + binary_string[position + 1:]
    
    error_value = struct.unpack('!f', int(binary_string, 2).to_bytes(4, 'big'))[0]
    
    return error_value

def calculate_fletcher_checksum(data):
    sum1 = 0
    sum2 = 0

    for byte in data:
        sum1 = (sum1 + byte) % 255
        sum2 = (sum2 + sum1) % 255

    checksum = (sum2 << 8) | sum1
    return checksum

def receive_data(serial_port, num_terms, error_detection):
    received_checksum = 0
    for i in range(num_terms):
        line = serial_port.readline().strip().decode('utf-8')
        if line == 'ovf':
            value = float('nan')  # Define um valor especial para representar overflow ('ovf')
        else:
            received_checksum = FletcherChecksumLib.FletcherChecksumStr.get_fletcher32(line)
            value = float(line)
            error = generateError()
            print("Índice do termo:", i+1)
            value = xor(value, error)
            if error_detection:
                after_checksum = FletcherChecksumLib.FletcherChecksumStr.get_fletcher32(value)
                if received_checksum == after_checksum:
                    print("Checksum verification: Failed")
                else:
                    print("Checksum verification: Passed")
            print("-------------------------------------------------") 


# Configuração da porta serial
serial_port = serial.Serial('COM4', 9600)  # Substitua 'COM4' pela porta serial correta do seu Arduino
time.sleep(2)  # Aguarda 2 segundos para estabilizar a comunicação serial

# Parâmetros do SCD
num_terms = 10  # Número de termos da progressão geométrica enviados pelo Arduino
error_detection = True  # Define se a deteção de erros será realizada (True) ou não (False)

# Recebe os dados do Arduino
received_data = receive_data(serial_port, num_terms, error_detection)

# Fecha a porta serial
serial_port.close()