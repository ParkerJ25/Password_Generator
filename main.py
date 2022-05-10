import random

chars = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%^&*()"


while 1:
    main
    print("Please note that password with length lower than 8 is not recommended for security reasons!")
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
           

    print("Note: recommended minimum password length is 8 characters")
    password_len = int(input("What length would you like your password to be :"))
    password_count = int(input("How many passwords would you like: "))
    for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is your password: ", password)
     main
