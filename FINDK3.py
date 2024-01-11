for t in range(int(input())):
    x,y,z=map(int,input().split())
    if((x*y)%z==0):
        a=x*y 
        b=z
        print(a,b)
    elif((x*z)%y==0):
        a=x*z 
        b=y 
        print(a,b)
    elif((y*z)%x==0):
        a=y*z 
        b=x 
        print(a,b)
    else:
        print(-1)