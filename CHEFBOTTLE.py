# cook your dish here
for t in range(int(input())):
    n,x,k=map(int,input().split())
    a=k//x 
    print(min(n,a))