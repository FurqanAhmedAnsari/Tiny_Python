print("Weight Convertor")
weight=input("Weight: ")

unit = input("""Weight you entered is in pound or kilogram?
(L)bs or (K)g: """)
if unit.upper() == "L":
   converted_weight = int(weight) // 2.205
   print(f"You are {converted_weight} kg")
elif unit.upper() == "K":
   converted_weight = int(weight) * 2.205
   print(f"You are {converted_weight} pounds")
else:
    print("Enter correct value")