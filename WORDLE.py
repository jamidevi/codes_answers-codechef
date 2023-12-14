# cook your dish here
for i in range(int(input())):
    s=list(input())
    t=list(input())
    m=[]
    for j in range(len(s)):
        if(s[j]==t[j]):
            m.append('G')
        else:
            m.append("B")
    print(''.join(m))        
            
    
