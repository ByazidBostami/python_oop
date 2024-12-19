times = int(input("Please input how many times you want to calculate :"))

max_sum = 0
temp = 0
my_list = []
for i in range(times):
    user = input("Please input something by space: ")
    checklist = list(map(int, user.split(" ")))
    check_sum = sum(checklist)
    
    if check_sum > temp:
        temp = check_sum
        my_list = checklist

print(temp,my_list)


    