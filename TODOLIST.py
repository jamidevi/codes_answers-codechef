# cook your dish here
for t in range(int(input())):
    n=int(input())
    d=list(map(int,input().split()))
    c=0
    for i in range(n):
        if(d[i]>=1000):
            c=c+1 
    print(c)
            
