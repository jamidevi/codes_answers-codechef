# cook your dish here
for t in range(int(input())):
    a,b=map(int,input().split())
    s=a+b 
    c=0
    for i in range(1,s+1):
        if(s%i==0):
            c+=1
    if(c==2):
        print("Alice")
    else:
        print("Bob")