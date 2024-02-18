# cook your dish here
for t in range(int(input())):
    x,y,m=map(int,input().split())
    r=x*m
    if(r<y):
        print("Yes")
    else:
        print("No")