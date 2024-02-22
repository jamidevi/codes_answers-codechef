# cook your dish here
for t in range(int(input())):
    n=int(input())
    if(n==1):
        print(1,1)
    elif(n%2==0):
        c=n//2
        
        print(c,n)
    else:
        c=(n//2)+1
        print(c,n)
        