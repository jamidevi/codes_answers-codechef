# cook your dish here
for t in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    c=1
    for i in range(n-1):
        if(s[i]!=s[i+1]):
            c+=1
    print(c)        