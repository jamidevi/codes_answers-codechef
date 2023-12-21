# cook your dish here
for t in range(int(input())):
    x,y=map(int,input().split())

    for i in range(y):
        x+=1   
    if(x%2==0):
        print("Janmansh")
    else:
        print("Jay")
        