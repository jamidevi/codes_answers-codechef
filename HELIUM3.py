# cook your dish here
for t in range(int(input())):
    a,b,x,y=map(int,input().split())
    c=a*b 
    u=x*y 
    if(u>=c):
        print("YES")
    else:
        print("NO")
    