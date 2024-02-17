# cook your dish here
for t in range(int(input())):
    x,y,z=map(int,input().split())
    total=x+y 
    if(x>z and total>z):
        print(0)
    elif(total<=z):
        print(2)
    else:
        print(1)
        
        