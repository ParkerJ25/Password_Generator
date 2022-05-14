import random
import string
from tkinter.messagebox import YES

chars = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%^&*()"
def print_2_file(password):
    if(file_flag == "Y"):
        pass_file = open("pass.txt", "a")
        pass_file.write(password + "\n")
    pass_file.close()


while 1:
    
    print("Please note that password with length lower than 8 is not recommended for security reasons!")
    file_flag = (input("Would you like your passwords to be stored in a file (Y/N)"))
    password_len = int(input("What length would you like your password to be :"))
    print("Would you like special characters? yes/no")
    if(input() == "yes"):
        chars = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    if (password_len < 8):
        print("The requested length is lower than 8, do you wish to continue anyway? yes/no")
        if (input() == "yes"):
            password_count = int(input("How many passwords would you like: "))
            for x in range(0,password_count):
                password = ""
                for x in range(0, password_len):
                    password_char = random.choice(chars)
                    password      = password + password_char
                print ("Here is your password: ", password)
                if(file_flag == "Y"):
                    print_2_file(password)
                else:
                    continue
        else:
            continue 
    else:
        password_count = int(input("How many passwords would you like: "))
        for x in range(0,password_count):
                password = ""
                for x in range(0, password_len):
                    password_char = random.choice(chars)
                    password      = password + password_char
                print ("Here is your password: ", password)
                if(file_flag == "Y"):
                    print_2_file(password)
                else:
                    continue     
