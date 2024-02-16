# cook your dish here
for t in range(int(input())):
    x,y=map(int,input().split())
    b=x//y 
    if(b<=20):
        print(b)
    else:
        print(20)