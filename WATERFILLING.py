# cook your dish here
for t in range(int(input())):
    b=list(map(int,input().split()))
    c=b.count(0)
    if(c>=2):
        print("Water filling time")
    else:
        print("Not now")
    