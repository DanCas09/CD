def MDC(D,d):
    r = D % d 
    while(r != 0):
        D = d
        d = r
        r = D % d
    return d

print("Máximo divisor comum:",MDC(348,156)) # 12