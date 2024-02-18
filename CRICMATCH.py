# cook your dish here
for t in range(int(input())):
    n,m=map(int,input().split())
    tr=m*6*6
    if(n<=tr):
        print("Yes")
    else:
        print("No")