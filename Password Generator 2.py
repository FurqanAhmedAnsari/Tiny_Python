import random

# Function to generate a password based on the specified number of alphabets, numbers, and symbols
def Password_Generator(x, y, z):
    # Define lists of alphabets, numbers, and symbols to choose from
    alphabets = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

    # Select x random alphabets, y random numbers, and z random symbols
    i = random.sample(alphabets, x)
    j = random.sample(numbers, y)
    k = random.sample(symbols, z)
    
    # Combine the selected characters into a single list
    a = i + j + k
    
    # Shuffle the list to randomize the order of characters
    random.shuffle(a)
    
    # Concatenate the characters to form the password
    return ''.join(a)

# Main code execution
print("Password Generator")
x = int(input("How many Alphabets would you like in your password: "))
y = int(input("How many numbers would you like in your password: "))
z = int(input("How many symbols would you like in your password: "))

# Generate and print the password
print(Password_Generator(x, y, z))