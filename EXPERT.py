# cook your dish here
for t in range(int(input())):
    x,y=map(int,input().split())
    a=(y/x)*100
    if(a>=50):
        print("YES")
    else:
        print("NO")