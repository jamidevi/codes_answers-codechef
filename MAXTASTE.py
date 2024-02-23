# cook your dish here
for t in range(int(input())):
    s=[]
    l=list(map(int,input().split()))
    for i in range(2):
        for j in range(2,4):
            c=l[i]+l[j]
            s.append(c)
    print(max(s))        
        
    