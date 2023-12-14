t = int(input())
for i in range(t):
    j = 1
    c = 0
    n = int(input())
    for k in range(1,n+1):
        j = k * (k+ 1)/2
        if  j> n:
            break
        else:
            c += 1
    print(c)
    
