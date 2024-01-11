# cook your dish here
for t in range(int(input())):
    a,b,c=map(int,input().split())
    if(c<a and c<b):
        print("Alice")
    elif(b<a and b<c):
        print("Bob")
    else:
        print("draw")