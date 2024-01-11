# cook your dish here
for t in range(int(input())):
    s=int(input())
    if(s<1500):
        hra=(s/100)*10 
        da=(s/100)*90
        gs=s+hra+da
        print(gs)
    else:
        hra=500 
        da=(s/100)*98 
        gs=s+hra+da 
        print(gs)
