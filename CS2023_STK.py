t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))  # Om's solved problems
    b = list(map(int, input().split()))  # Addy's solved problems
    
    max_streak_om = 0
    max_streak_addy = 0
    current_streak_om = 0
    current_streak_addy = 0
    
    for i in range(n):
        if a[i] > 0:  # If Om solved a problem on day i
            current_streak_om += 1
            max_streak_om = max(max_streak_om, current_streak_om)
        else:
            current_streak_om = 0
        
        if b[i] > 0:  # If Addy solved a problem on day i
            current_streak_addy += 1
            max_streak_addy = max(max_streak_addy, current_streak_addy)
        else:
            current_streak_addy = 0

    if max_streak_addy > max_streak_om:
        print("ADDY")
    elif max_streak_addy == max_streak_om:
        print("DRAW")
    else:
        print("OM")
    
    t -= 1
