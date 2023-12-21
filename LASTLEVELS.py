# cook your dish here
for t in range(int(input())):
    x,y,z=map(int,input().split())
    if(x>3):
        if(x%3==0):
        
            q=(x//3)-1
            print((x*y)+(q*z))
        else:
            q=(x//3)
            print((x*y)+(q*z))
            
    else:
        print(x*y)