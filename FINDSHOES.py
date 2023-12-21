# cook your dish here
for t in range(int(input())):
    n,m=map(int,input().split())
    if(m>n):
        print(n)
    else:
        print((n-m)+n)
