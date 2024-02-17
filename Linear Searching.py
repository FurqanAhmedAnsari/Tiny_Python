my_list = [44, 74, 24, 94, 14, 54, 84]
target_number = int(input("Enter a number to find: "))
for i in range(len(my_list)):
    if target_number in my_list:
        if my_list[i] == target_number:
            print(f"Number {target_number} found at index {i}")
    else:
        print(f"Number {target_number} is not in the list.")
        break