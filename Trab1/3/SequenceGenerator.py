import random
import math

# change genericSource
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


# H(X) = - ∑ p(x) log2 p(x)
def estimatedEntropy(px):
    H = 0
    for p in px:
        if p > 0:
            H -= p * math.log2(p)
    return H

# H'(X) = - ∑ f(x)/N log2 f(x)/N
def entropy(string, symbols):
    freq = {s: 0 for s in symbols}  # Initialize frequency dictionary
    for s in string:
        if s in freq:
            freq[s] += 1
        else:
            freq[s] = 1
    H_est = 0
    for s in symbols:
        p_s = freq[s] / len(string)
        H_est -= p_s * math.log2(p_s)
    return H_est



def main():
    px = [0.4,0.2,0.3,0.1] # Função Massa de Probabilidade
    symbols = ['a','b','c','d'] 
    sizes = [100, 1000, 10000, 100000] # diferentes dimensões N
    for size in sizes:
        string = genericSource(px, size, symbols)
        H_est = estimatedEntropy(px)
        H = entropy(string, symbols)
        print(f"Size: {size}\nReal entropy: {H}\nEstimated entropy: {H_est}\n")

main()
