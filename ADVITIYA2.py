# cook your dish here
def Judged(response):
    c=response.count(1)
    if(c>=4):
        print("Yes")
    else:
        print("No")
for t in range(int(input())):
    RL=list(map(int,input().split()))
    Judged(RL)
