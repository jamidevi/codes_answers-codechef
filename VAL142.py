# cook your dish here
def gift(budget):
    # Calculate the total cost of gifts for all 7 days using the formula forthesum of a geometric series
    total_amount=(2**7-1)   # 2^7 - 1 is the sum of a geometric series with 7 terms
    if total_amount<=budget:
        return "Yes"
    else:
        return "No"
for t in range(int(input())):
    x=int(input())
    result=gift(x)
    print(result)
    
