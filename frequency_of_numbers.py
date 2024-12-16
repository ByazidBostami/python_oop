flag = True
my_list = []
# count = 0
# checklist = my_list
while flag == True:
    user = input("Please input something: ")
    if user == "Stop":
        flag = False
    else:
        my_list.append(user)
check_list = {}
for i in my_list:
    if i in check_list:
        check_list[i] += 1
    else:
        check_list[i] = 1

for k , v in check_list.items():
    print(f"{k} -{v} times ")
    
    





