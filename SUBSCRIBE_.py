# cook your dish here
for t in range(int(input())):
    n,x=map(int,input().split())
    if(n==1):
        print(x)
    elif(n%6==0):
        s=n//6
        ts=s*x 
        print(ts)
    else:
        s=(n//6)+1
        ts=s*x 
        print(ts)
