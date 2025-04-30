import random
import math

def genericSource(px, M, symbols):
    px_sum = sum(px)
    px = list(map(lambda i: i / px_sum, px))
    px = list(map(lambda i: i * M, px))
    string = ""
    while len(string) < M:
        i = random.choices(range(len(px)), weights=px)[0]
        string += symbols[i]
        px[i] -= 1
        if px[i] == 0:
            del px[i]
            del symbols[i]
    return string

def generatePassword():
    px = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05] # Probability Mass Function
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', '1', '2', '3', '4'] # Alphabet
    length = random.randint(8, 12)
    password = genericSource(px, length, symbols)
    return password

def main():
    for i in range(5):
        password = generatePassword()
        print(f"Password {i+1}: {password}")

main()
