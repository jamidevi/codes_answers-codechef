# cook your dish here
def minimum_time_bullet(speed_bullet,away_time,wait_time):
    reach_time=away_time//speed_bullet
    start_after=wait_time-reach_time
    return start_after 
for t in range(int(input())):
    x,y,z=map(int,input().split())
    result=minimum_time_bullet(x,y,z)
    if( result>0):
        print(result)
    else:
        print(0)
    
    
