list = [12 ,15 ,20 ,25 ,31 ,65 ,77 ,86 ,88 ,91 ,92 ,95 ,100]
number = int(input("Enter a number: "))
start = 0
end = len(list)-1

while start <= end:
    mid_point = (start + end) // 2
    if number == list[mid_point]:
        print(f"{number} is in the list at index {mid_point}")
        break
    
    if number < list[mid_point]:
        end = mid_point - 1
    
    else:
        start = mid_point + 1

else:
    print(f"{number} is not in the list")