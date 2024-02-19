# cook your dish here
for t in range(int(input())):
    n=int(input())
    tm=n*50              #total money he earned for selling n juices 
    sm=(tm*(20/100))+(tm*(20/100))+(tm*(30/100))
    print(int(tm-sm))