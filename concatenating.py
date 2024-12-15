def concatenating(user_1, user_2):
    new_str = ""
    
    
    count = 0
    for i in user_1:
        if i in user_2:
            new_str += i
            count += 1

    for j in user2:
        if j in user1:
            new_str += j    

    if count == 0:
        return "Nothing in common."
        
    else:
        return new_str

user1 = input("Please input first output: ")
user2 = input("Please input second output: ")

print(concatenating(user1, user2))
