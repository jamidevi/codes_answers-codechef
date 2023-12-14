# cook your dish here
for t in range(int(input())):
    n=int(input())
    r=0
    temp=n
    while(temp>0):
        r=(r*10)+(temp%10)
        temp=temp//10
    if(r==n):
        print("wins")
    else:
        print("loses")