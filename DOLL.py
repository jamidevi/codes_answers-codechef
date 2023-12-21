# cook your dish here
for t in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in range(len(l)):
        if(l[i]>k):
            c=c+1
    print(c)            
