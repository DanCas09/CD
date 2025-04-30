def geometric_prog(u, r, n):
    res = []
    numbers = list(range(n))
    for i in range(1, n):
        res.append(u * pow(r,(i-1)))    #a(n) = u*r^(n-1)
    return res

print(geometric_prog(3, 2, 10))
