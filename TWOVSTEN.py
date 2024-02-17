# Loop through each test case
for _ in range(int(input())):
    # Initialize the number of turns to 0
    t = 0
    # Input the initial value of X
    x = int(input())
    
    if(x%10 ==0):
        print(0)
    elif(x%5 ==0):
        print(1)
    else:
        print(-1)