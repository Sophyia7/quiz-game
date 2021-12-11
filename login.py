# Import JSON
import json

from quiz import start, quiz

# this saves user email as an object so I could use it later in the program

with open('user.json', 'r') as y:
    database = y.read()
    database = json.loads(database)

    user_Email = None


# This function initializes the program

def init():
    # while True:
    print("Welcome!")
    user_sign = input("Do you have an account? l. Login or r. Register: \n")

    if user_sign.lower() == "l":
        login()
        # this directs the user to login

    elif user_sign.lower() == "r":
        register()
        # this directs the user to register

    else:
        print("Invalid Input, Use the correct letter.")
        init()
        # this prompts the user to type the valid letter to access the quiz system


# this is the registration function

def register():
    print("Okay, registering a new user")
    email = input("Enter your email address: \n")
    password = input("Enter your password: \n")
    repeat_password = input("Repeat your password: \n")

    # this checks if email has been used by another user
    with open('user.json', 'r') as f:
        db = f.read()
        db = json.loads(db)

    if email in db:
        print(email + " has already been taken")
        register()

    # this checks if the inputted password is same thing
    if password == repeat_password:
        print("Congratulations, " + email + " has been successfully registered")

        # this saves the user info into a json file called "users.json"
        with open('user.json', 'r') as infile:
            db = infile.read()
            db = json.loads(db)
            db[email] = {
                "password": password,
                "score": 134
            }

        with open("user.json", 'w') as outfile:

            json.dump(db, outfile)

        login()  # this directs user to login after saving info to users.json
    else:
        print("Sorry, The two passwords don't match")
        register()

    # this is the login function


def login():
    print("Okay, you are now logging in")
    login_email = input("Enter your email address: \n")
    login_password = input("Enter your password: \n")

    # this checks if the inputted email and password is same as the information used to register
    with open('user.json', 'r') as infile:
        db = infile.read()
        db = json.loads(db)

        if login_email in db:
            if login_password == db[login_email]["password"]:
                print("Welcome " + login_email +
                      f" . You have {db[login_email]['score']} Points.")
                start(login_email)
                quiz(login_email)
                end_game()
            else:
                print("Your user name and password doesn't match1")
                login()
        else:
            print("No such user exists")
            login()


def end_game():
    print("End of Quiz!")


init()
