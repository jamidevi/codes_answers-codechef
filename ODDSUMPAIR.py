# cook your dish here
for t in range(int(input())):
    a,b,c=map(int,input().split())
    if((a+b)%2!=0):
        print("yes")
    elif((a+c)%2!=0):
        print("yes")
    elif((b+c)%2!=0):
        print("yes")
    else:
        print("No")