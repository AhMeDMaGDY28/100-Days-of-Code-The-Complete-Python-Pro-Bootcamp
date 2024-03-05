#!/usr/bin/python3
"""a game for fun and seeing what your choices will do"""
import sys
print("Welcome to Treasure Island")
print("your misssion is to find the treasure")
first_choice = "waiting for input"
first_choices_list = ["right", "left"]
second_choices_list = ["wait", "swim"]
second_choice = "waiting for input"
third_choices_list = ["red", "blue", "pink"]
third_choice = "waiting for input"
while first_choice not in first_choices_list:
    first_choice = input(
            "you are at a cross road. where do you want to go? Type < left > or < right >\n"
            )
    if (first_choice == "right"):
        print(" you have encountered a giant Python and died")
        sys.exit()
    elif (first_choice == "left"):
        print("you came to a lake. and saw an island in the middle of the lake")
        break
    else:
        print("wrong answer you have 2 ways to choose from which is right or left")
        print("choose again carefully")
while second_choice not in second_choices_list:
    print("do you want to swim or to wait for a boat")
    second_choice = input("Type <swim> to swim or <wait> to wait for boat\n")
    if (second_choice == "swim"):
        print("while you swam you have awakend a sleeping dragon in the lake and he ate you")
        print("you are dead")
        sys.exit()
    elif (second_choice == "wait"):
        print("a boat came and you reached the island")
        break
    else:
        print("wrong answer you have 2 ways to choose from which is swim or wait")
        print("choose again carefully")
while third_choice not in third_choices_list:
    print("you saw a house with 3 doors which red, pink, blue")
    third_choice = input("which colour you choose?\n")
    if (third_choice == "red"):
        print("you found a gang of beasts looking at you")
        print("they attacked you and ate you alive")
        print("you are dead")
        sys.exit()
    elif (third_choice == "pink"):
        print("you found a banshie having a bath and when she saw you she screamed and your brain exploded")
        print("you are dead")
        sys.exit()
    elif (third_choice == "blue"):
        print("you found a treasure in the room")
        print("you went to open the treasure")
        print("you went to open the treasure and found that the treasure is empty so you killed your self")
        print("you are dead")
        sys.exit()
    else:
        print("wrong answer you have 3 doors to choose from which is pink or red or blue")
        print("choose again carefully")
