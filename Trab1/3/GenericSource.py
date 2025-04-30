import random

def genericSource(px,M,symbols):
    px_sum = sum(px)
    px = list(map(lambda i: i / px_sum, px))
    px = list(map(lambda i: i * M,px))
    f = open("AAAAA.txt","w")
    string = ""
    while len(string) < M:
        i = random.randint(0, len(px) - 1)
        string += symbols[i]
        px[i] -= 1
        if(px[i] == 0):
            del px[i]
            del symbols[i]
        
    f.write(string)
    f.close()


def main():
    px = [0.4,0.2,0.3,0.1] # Função Massa de Probabilidade
    symbols = ['a','b','c','d'] # 
    M = 10000
    genericSource(px,M,symbols)

main()