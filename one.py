# higher lower game

import oneArt
import oneData 
import random


def frame () :
    print(oneArt.logo)

global nextPerson
def game () :
    dead = False
    currentPerson = 0
    nextPerson = 0
    while not dead :
        frame()
        currentPerson = nextPerson
        nextPerson = round(random.random()*(len(oneData.data)-1))
        if nextPerson == currentPerson:
            nextPerson+=1
        print("Who do you think has more followers?")
        print()
        print()
        print(f"{oneData.data[currentPerson]["name"]}, a {oneData.data[currentPerson]["description"]} from the {oneData.data[currentPerson]["country"]}")
        print(oneArt.orr)
        print(f"{oneData.data[nextPerson]["name"]}, a {oneData.data[nextPerson]["description"]} from the {oneData.data[nextPerson]["country"]}")
        print()
        print()
        print()
        print("A or B?")
        print()
        answered = False
        answer = ""
        answer = input()
        if answer == "A" or answer == "B" :
            answered = True
        if not answered:
            while not answered :
                answer = input()
                if answer == "A" or answer == "B" :
                    answered = True
        print()
        print(f"{oneData.data[currentPerson]["name"]} has {oneData.data[currentPerson]["follower_count"]}, and ")
        print()
        print(f"{oneData.data[nextPerson]["name"]} has {oneData.data[nextPerson]["follower_count"]}.")
        print()
        print()
        if( answer == "A"):
            if((oneData.data[currentPerson]["follower_count"]) > (oneData.data[nextPerson]["follower_count"])):
                print("Correct!")
            else:
                print("Incorrect!")
                dead=True
        else:
            if((oneData.data[nextPerson]["follower_count"]) > (oneData.data[currentPerson]["follower_count"])):
                print("Correct!")
            else:
                print("Incorrect!")
                dead=True

game()