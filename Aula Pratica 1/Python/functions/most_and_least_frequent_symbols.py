from collections import Counter
import sys

def most_and_least_frequent_symbols(file):
    with open(file, 'r') as f:

        contents = f.read().replace('\n', '')
        symbol_counts = Counter(contents)
        
        letterM, countM = symbol_counts.most_common(1)[0]
        letterL, countL = symbol_counts.most_common()[-1]
        
        print(f"Most common symbol: {letterM}, count: {countM}")
        print(f"Least common symbol: {letterL}, count: {countL}")

def main():
    most_and_least_frequent_symbols(sys.argv[1])

main()
