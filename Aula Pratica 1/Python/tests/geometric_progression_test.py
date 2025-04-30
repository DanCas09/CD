from geometric_progression import geometric_prog

def gp_test1():
    u = 3
    r = 2
    n = 10
    gp = geometric_prog(u,r,n)
    next = u
    for i in range(0, len(gp)):
        if(gp[i] !=  next):
            print('Test1 Failed!')
            return
        next = next * r
    print('Test1 Succeeded!')

gp_test1()