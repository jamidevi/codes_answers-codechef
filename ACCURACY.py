# cook your dish here
for t in range(int(input())):
    x=int(input())
    k=x%3
    if(k%3==0):
        print(k%3)
    else:
        print(3-k%3)