# cook your dish here
for t in range(int(input())):
    n,x=map(int,input().split())
    if(x%n==0):
        print("Yes")
    else:
        print("No")