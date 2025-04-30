from VernamCypher import makeVernamCypher
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import random
import math


def entropy(px): # Counter({'a': 0.45, 'b': 0.25, 'd': 0.15, 'c': 0.15})
    H = 0
    for char in px:
        H += px[char] * personalInfo(px[char])
    return H

def px(arr):
    c = Counter(arr)
    total = len(arr)
    for char in c:
        c[char] = c[char] / total
    return c

def personalInfo(p):
    return -math.log2(p)     # -log2(p(x))

def readFile(f):
    if(".bmp" in f) :
        a = readbmp(f)
    else:
        with open(f,'r') as f:
            a = f.read().replace('\n','')
            #a = a.replace(' ','') #if dont take ' ' it takes a while to create the histogram
    return a

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


# read in the plaintext from the Alice in Wonderland file
fileName = "../TestsFiles/alice29.txt"
with open(fileName, "r") as file:
    plaintext = file.read()

# entropy of file
    counter = readFile(fileName)
    fmp = px(counter)
    print(f"Entropy is {entropy(fmp)}")

# define the bin size for the histograms
bin_size = 10

# create a histogram of the plaintext
plaintext_hist, plaintext_bins = np.histogram([ord(c) for c in plaintext], bins=range(0, 256, bin_size))
plt.bar(plaintext_bins[:-1], plaintext_hist, align='edge', width=bin_size)

# add labels to the plaintext histogram
plt.xlabel("ASCII Code")
plt.ylabel("Frequency")
plt.title("Plaintext Histogram")

# display the plaintext histogram
plt.show()

# define the keys for the Vernam cipher
constKey = ""
for i in range(0, len(plaintext)):
    constKey += "a"

randomKey = genericSource(px = [0.3,0.2,0.3,0.1,0.1], M = len(plaintext), symbols = ['a','b','c','d','e'])

# encrypt the plaintext using the Vernam cipher with constant key
ciphertext = makeVernamCypher(plaintext, constKey)

# create a histogram of the ciphertext
ciphertext_hist, ciphertext_bins = np.histogram([ord(c) for c in ciphertext], bins=range(0, 256, bin_size))
plt.bar(ciphertext_bins[:-1], ciphertext_hist, align='edge', width=bin_size)

# add labels to the ciphertext histogram
plt.xlabel("ASCII Code")
plt.ylabel("Frequency")
plt.title("Ciphertext Histogram")

# display the ciphertext histogram
plt.show()

# encrypt the plaintext using the Vernam cipher with random key
ciphertext = makeVernamCypher(plaintext, randomKey)

# create a histogram of the ciphertext
ciphertext_hist, ciphertext_bins = np.histogram([ord(c) for c in ciphertext], bins=range(0, 256, bin_size))
plt.bar(ciphertext_bins[:-1], ciphertext_hist, align='edge', width=bin_size)

# add labels to the ciphertext histogram
plt.xlabel("ASCII Code")
plt.ylabel("Frequency")
plt.title("Ciphertext Histogram")

# display the ciphertext histogram
plt.show()
