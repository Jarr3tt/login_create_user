import time

user_dir = ["admin","guest",]
pass_dir = ["root","",]
while True:
    print("Would you like to login to an existing account or create a new user?")
    userInput = input("> ")
    if userInput == "new user":
        print("Please enter a username.")
        newUser = input("USER: ")
        print("Now enter a password.")
        newPass = input("PASS: ")
        print("Please re-enter your password to confirm.")
        checkPass = input("RE-ENTER: ")
        if checkPass == newPass:
            user_dir.append(newUser)
            pass_dir.append(newPass)
            print("Your username and password have been saved!")
            print("Returning to the login line...")
            time.sleep(1)
            continue
        else:
            print("Your password did not match the re-entry!")
            print("Returning to the login line...")
            continue
    elif userInput == "existing account":
        print("What is your username?")
        userLogin = input("USER: ")
        print("What is your password?")
        passLogin = input("PASS: ")
        if userLogin in user_dir:
            user2 = user_dir.index(userLogin)
            pass2 = pass_dir.index(passLogin)
            if user2 == pass2:
                if passLogin in pass_dir:
                    print("Welcome!")
                    break
                else:
                   print("Wrong username or password! Returning...")
                   continue
            else:
                print("Wrong username or password! Returning...")
                continue
        else:
            print("Wrong username or password! Returning...")
            continue
    else:
        print("Command not understood. Returning to entry line...")
        continue
