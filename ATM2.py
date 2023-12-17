# cook your dish here
for t in range(int(input())):
    n,k=map(int,input().split())
    s=""
    l=list(map(int,input().split()))
    for i in range(n):
        if k>= l[i]:
            k-=l[i]
            s+="1" 
        else:
            s+="0"
    print(s)        
            