

def extract_substring(user):
    f_index = 0
    l_index = 0
    count = 0
    for i in range(len(user)):
        if user[i].isupper():
            f_index = i 
            break
    for j in range(f_index,len(user)):
        if user[j].isupper():
            l_index = j
    if l_index - f_index == 1:
        
        return "BLANK"      
    else:
    
        return user[f_index+1:l_index:1]
    
user = input("Please input Something :")
print(extract_substring(user))
            
            


        
    
            