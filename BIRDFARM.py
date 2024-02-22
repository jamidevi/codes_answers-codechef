# cook your dish here
for t in range(int(input())):
    x,y,z=map(int,input().split())
    if(x==z and y==z):
        print("Any")
    elif(z%x!=0 and z%y!=0):
        print("None")
    elif(z%x==0 and z%y!=0):
        print("Chicken")
    elif(z%x !=0 and z%y ==0):
        print("Duck")
    else:
        print("Any")
