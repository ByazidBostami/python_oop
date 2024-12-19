myList = [2,3,6]
myList_2 = [3,4,5]

final_list = []

for i in myList:
    for j in myList_2:
        final_list.append(i*j)

print(final_list)