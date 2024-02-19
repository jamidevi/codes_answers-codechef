# cook your dish here
for t in range(int(input())):
    n,x=map(int,input().split())
    if (n*x) % 4 == 0:
        print(int((n*x)/4))
    else:
        print(int((n*x)/4)+1)