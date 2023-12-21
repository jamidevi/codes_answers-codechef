# cook your dish here
for t in range(int(input())):
    s=input()
    c='Sad'
    for i in range(len(s)-2):
        if(s[i] in {'a','e','i','o','u'}):
            if(s[i+1] in {'a','e','i','o','u'}):
                if(s[i+2] in {'a','e','i','o','u'}):
                    c='Happy'
                    break
    print(c)            
            
    
