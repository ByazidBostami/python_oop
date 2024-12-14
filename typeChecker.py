def typeCheck(user):
    is_Num = False
    is_Alp = False

    for i in user:
        ascii_value = ord(i)
        if 48 <= ascii_value <= 57:
            is_Num = True

        if 65 <= ascii_value <= 90 or 97 <= ascii_value <= 122:
            is_Alp = True

    # if is_Num == True:
    #     print("Number")
    # elif is_Alp == True:
    #     print("Word")
    # elif is_Alp == True and is_Num == True:
    #     print("Mixed")

    
    if is_Alp and is_Num:
        print("Mixed")
    elif is_Num:
        print("Number")
    elif is_Alp:
        print("Word")

user = input("Please enter something for check: ")

typeCheck(user)