# cook your dish here
for t in range(int(input())):
    a,b,c=map(int,input().split())
    average=(a+b)/2
    if(average>c):
        print("Yes")
    else:
        print("NO")