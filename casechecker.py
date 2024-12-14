

def caseChecker(user):
    count = 0
    count_U = 0
    for i in user:
        if i.islower():
            count += 1
        if i.isupper():
            count_U += 1

    if count < count_U:
        print(user.upper())
    if count_U < count:
        print(user.lower())

user = input("Please input a Word for check :")
caseChecker(user)

    
