# cook your dish here
for t in range(int(input())):
    n=int(input())
    rn=0
    while(n>0):
        r=n%10
        rn=(rn*10)+r 
        n=n//10
    print(rn)    
        