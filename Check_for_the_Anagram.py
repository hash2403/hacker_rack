str1=input()
str2=input()

if len(str1)==len(str2):
    sort_str1=sorted(str1)
    sort_str2=sorted(str2)
    
    if sort_str1==sort_str2:
        print("true")
    else:
        print("false")
        
else:
    print("false")
