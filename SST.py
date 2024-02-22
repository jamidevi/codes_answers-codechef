# cook your dish here
for t in range(int(input())):
    a,b=map(int,input().split())
    fi=(100//10)*a 
    si=(100//20)*b 
    if(fi>si):
        print("First")
    elif(fi<si):
        print("second")
    else:
        print("Any")
        