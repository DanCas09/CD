from statistics import mean

def cod(str):
    res = ''
    for i in range(len(str)):
        curr = str[i]
        while len(curr) < 3:
            curr += str[i]
        res += curr
    return res

def decod(str):
    res = ''
    curr = ''
    for i in range(len(str)):
        curr += str[i]
        if( len(curr) == 3):
            inteiros = [int(num) for num in curr]
            average = mean(inteiros)
            rounded = round(average, 0)
            inteiro = int(rounded)
            res += f'{inteiro}' # média do curr
            curr = ''
    return res

#def main():
#    print(cod("110")) # 111111000
#    print(decod("000111000")) #010
    
#main()