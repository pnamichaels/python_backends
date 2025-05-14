my_list = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
count = 1

while count <= 3:
    for i in my_list:
        if i == "Monday":
            continue
        print(i, "\n")
    print("---------------------------------")
    count += 1