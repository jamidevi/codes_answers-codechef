# cook your dish here
for t in range(int(input())):
    x,a,b=map(int,input().split())
    s=(a*1)+(b*2)
    if(s>=x):
        print("Qualify")
    else:
        print("NotQualify")