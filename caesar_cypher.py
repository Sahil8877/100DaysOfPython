import string
letters = string.ascii_letters
print("C A E S A R\nC Y P H E R")

def encrypt(string_to_encrypt,shift):
    string_after_encryption = ""
    
    for i in string_to_encrypt:
        if str(i).isalpha():
            string_after_encryption += letters[(letters.index(i)+shift)%26]
        else:
            string_after_encryption += i
    return string_after_encryption

def decrypt(string_to_decrypt,shift):
    string_after_decryption = ""
    for i in string_to_decrypt:
        if str(i).isalpha():
            string_after_decryption += letters[(letters.index(i)-shift)%26]
        else:
            string_after_decryption += i
    return string_after_decryption

def ceasar():
    run = True
    while run:
        user_choice = input("Press E to encode or D to decode :").lower()
        if user_choice == 'E' or user_choice == 'e':
            string_to_encrypt = input("Enter text to encrypt :")
            shift = input("Enter amount of shift :")
            if shift.isnumeric():
                encrypted_string = encrypt(string_to_encrypt,int(shift))
                print(encrypted_string)
                ask_to_continue = input("Would you like to continue? y/n:").lower()
                if ask_to_continue == 'y':
                    continue
                else:
                    run = False
            else:
                print("Invalid input for shift!")
                continue
        
        elif user_choice == 'D' or user_choice == 'd':
            string_to_decrypt = input("Enter text to decrypt :")
            shift = input("Enter amount of shift :")
            if shift.isnumeric():
                decrypted_string = decrypt(string_to_decrypt,int(shift))
                print(decrypted_string)
                ask_to_continue = input("Would you like to continue? y/n:").lower()
                if ask_to_continue == 'y':
                    continue
                else:
                    run = False
            else:
                print("Invalid input for shift!")
                continue
        else:
            print("invalid input!")
            continue
        
ceasar()