# cook your dish here
for _ in range(int(input())):
    N, K = map(int, input().split())
    
    # Possible slice counts per orange
    slice_options = [10, 11, 12]
    
    # Initialize a set to store possible total slice counts with N oranges
    possible_sums = {0}
    
    # For each orange, expand possible sums by adding each slice option
    for _ in range(N):
        current_sums = set()
        for s in possible_sums:
            for slices in slice_options:
                current_sums.add(s + slices)
        possible_sums = current_sums
    
    # Check if K is in the set of possible sums
    if K in possible_sums:
        print("YES")
    else:
        print("NO")
