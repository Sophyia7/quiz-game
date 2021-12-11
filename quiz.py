# TODO:
# Play Game:
# 1. Show user their initial score at the beginning of the game
# 2. Prompt user to select number of questions
# 3. Get number of questions from quiz API
# 4. Display questions and options
# 5. Update user score based on answers
# 6. Display end quiz message and updated score
# 7. Save score to database


# from login import init
import json

import requests


r = requests
website = r.get("https://opentdb.com/api.php?amount=10&type=multiple")

website = website.json()


def quiz(email):
    with open("user.json", 'r') as f:
        db = f.read()
        db = json.loads(db)
        points = db[email]["score"]

    person_input = int(
        input("How many questions do you want to answer in this session? \n"))
    print("Retrieving questions from opentd...")

    # this takes user input and slices the question
    outputs = website["results"][0: person_input]

    # this saves the length of user input to extract the questions and answers
    counter = len(outputs)

    # this loops through the user desired input and drops a question for user to answer
    for i in range(counter):
        print(outputs[i]["question"])

        option_1 = (outputs[i]["incorrect_answers"])
        option_2 = (outputs[i]["correct_answer"])

        option_1.append(option_2)
        print("Options are: ")
        options_dict = {}
        option_list = ["A", "B", "C", "D", "E", "F"]
        j = 0
        for option in option_1:
            options_dict[option_list[j]] = option
            print(f"{option_list[j]}. {option}")
            j += 1

        # this is the var for correct answer
        answer = (outputs[i]["correct_answer"])
        user_key = input("Enter your answer: \n")

        # this is to make sure user inputs an alphabet and not words
        if user_key in options_dict:
            user_answer = options_dict
        else:
            print("Wrong Option")
            user_answer = ''

        if user_answer == answer:
            points += 5
            print("Correct. You now have " + str(points) + " points.")
        else:
            points -= 3
            print("Wrong! You now have " + str(points) + " points")

        db[email]["score"] = points

        with open("user.json", "w") as jsonFile:
            json.dump(db, jsonFile)


def start(email):
    quiz(email)
    print("End of Quiz!")

    with open('user.json', 'r') as f:
        db = f.read()
        db = json.loads(db)

    print("Goodbye " + email + " Your current Score " + f"{db[email]['score']}" + " points has been stored")
    exit()
