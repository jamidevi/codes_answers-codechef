# cook your dish here
for t in range(int(input())):
    x,y,z=map(int,input().split())
    if(x%y==0):
        print((x//y)*z)
    else:
        print(((x//y)+1)*z)