# cook your dish here
for t in range(int(input())):
    x=int(input())
    tc=0
    fc=0
    if(x%10==0 and  x%5 ==0):
        tc=x//10
        print(tc)
    elif(x%5==0 and x%10!=0):
        s=x%10
        tc=x//10
        if(s%5==0):
            fc=s//5
            print(tc+fc)
    else:
        print(-1)
        