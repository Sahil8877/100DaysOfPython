import random
letters = ['A','B','C','D']
numbers = [1,2,3,4]
symbols = ['_','#','@','*']

print("Welcome to Password Generator")

num_letters = int(input("How many leters you want :"))
num_numbers = int(input("How many numbers you want :"))
num_symbols = int(input("How many symbols you want :"))

random_letters = random.sample(letters,num_letters)
random_numbers = random.sample(numbers,num_numbers)
random_symbols = random.sample(symbols,num_symbols)

password = random_letters + random_numbers + random_symbols
random.shuffle(password)

final_password = ""

for chars in password:
    final_password += str(chars)

print("Your Password :",final_password)