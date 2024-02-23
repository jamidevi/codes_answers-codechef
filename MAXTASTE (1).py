# cook your dish here
for t in range(int(input())):
    l=list(map(int,input().split()))
    max_taste=max(l[0]+l[2],l[0]+l[3],l[1]+l[2],l[1]+l[3])  
    print(max_taste)
        
    