my_list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",]
count = 1

while count <= 3:
    for i in my_list:
        if i == "Monday":
            print('We dont speak of this day')
        else:
            print(i)
    
    count += 1