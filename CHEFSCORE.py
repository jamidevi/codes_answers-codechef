# cook your dish here
for t in range(int(input())):
    n,x,y=map(int,input().split())
    print("Yes") if(y%x==0) else print("No")
