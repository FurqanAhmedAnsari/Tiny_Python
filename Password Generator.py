import random

def Password_Generator():
    password = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U',
                'I', 'O', 'P', 'A', 'S', 'D', 'F',
                'G', 'H', 'J', 'K', 'L', 'Z', 'X',
                'C', 'V', 'B', 'N', 'M','q', 'w', 
                'e', 'r', 't', 'y', 'u', 'i', 'o',
                'p', 'a', 's', 'd', 'f', 'g', 'h',
                'j', 'k', 'l', 'z', 'x', 'c', 'v',
                'b', 'n', 'm', '1', '2', '3', '4',
                '5', '6', '7', '8', '9', '!', '@',
                '#', '$', '%', '^', '&', '*']

    x = random.sample(password,12)
    x = ''.join(x)
    return x

# --------main----------#

print("Password Generator")
print(Password_Generator()) 