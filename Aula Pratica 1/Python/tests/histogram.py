import math 
from collections import Counter
import sys
import matplotlib.pyplot as plt
from PIL import Image

def printPI(counter):
    for char in counter:
        currPI = personalInfo(counter[char])
        print(f"Symbol {char} : {currPI}")
    

def personalInfo(p):
    return -math.log2(p)     # -log2(p(x))

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


def readbmp(file):
    im = Image.open(file)
    pix_val = list(im.getdata())
    return pix_val
    
def createHist(arr,nrOfBins,name): 
    plt.style.use('ggplot')
    plt.hist(arr,bins=nrOfBins) # total
    plt.title(f"Histogram of {name}")
    plt.xlabel("Symbols")
    plt.ylabel("Frequency")
    plt.show()

def readFile(f):
    if(".bmp" in f) :
        a = readbmp(f)
    else:
        with open(f,'r') as f:
            a = f.read().replace('\n','')
            a = a.replace(' ','') #if dont take ' ' it takes a while to create the histogram
    return a

def showResults(fileName):
    #f = sys.argv[1]
    #fileName = f.split('\\')[-1]
    String = readFile(fileName) # nota no caso da lena é um array de inteiros "tons de cinza".
    
    fmp = px(String) # ['a':0.2, 'b':0.4, 'c':0.3, 'd':0.1]
    
    printPI(fmp)
    H = entropy(fmp)
    print(f"Entropy is {H}")
    
    return H, list(String)

#def main():
#    fileName = './testFiles/test_file_5d.txt'
#    H, list = showResults(fileName)
#    createHist(list,255,fileName)

#main()