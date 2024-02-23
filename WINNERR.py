# cook your dish here
for t in range(int(input())):
    pa,pb,qa,qb=map(int,input().split())
    p=max(pa,pb)
    q=max(qa,qb)
    if(p<q):
        print("P")
    elif(p==q):
        print("Tie")
    else:
        print("Q")
        