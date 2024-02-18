# cook your dish here
for t in range(int(input())):
    p,l=map(int,input().split())
    lr=(l/p)*100
    if(lr>=75):
        print("Yes")
    else:
        print("No")