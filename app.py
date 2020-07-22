import random
import os

try:

    os.system("cls")
    os.system("color c")


    print("-----------------------------")
    print("Tool made by dezerr")
    print("-----------------------------\n")
    numberOfPlayer = input("What is the number of players ? : ")
    numberOfPlayer = int(numberOfPlayer)
    

    def shuffler():
        i = 0
        iPlusOne = i + 1
        # Table containing all the players
        arrNameOfPLayer = []

        while i < numberOfPlayer:
            nameOfPlayer = input("What's the name of the player " + str(iPlusOne)  + " ? : ")
            arrNameOfPLayer.append(nameOfPlayer)
            i = i + 1
            iPlusOne = iPlusOne + 1

        print("\nThe players are : " + str(arrNameOfPLayer))
        random.shuffle(arrNameOfPLayer)
        print("\nThe players were randomly shuffled : " + str(arrNameOfPLayer) + "\n")


        # Séparation d'équipes
        numberOfTeam = input("How many teams do you want ? : ")
        numberOfTeam = int(numberOfTeam)
        test = numberOfPlayer % numberOfTeam

        if test == 0:
            pad = len(arrNameOfPLayer) / numberOfTeam
            pad = int(pad)
            aS = [arrNameOfPLayer[i:i+pad]for i in range(0, len(arrNameOfPLayer) - pad + 1, pad)]
            print("Here are the " + str(numberOfTeam) + " teams : \n")
            print(aS)
            print("\n")
        else:
            print("That's not possible.")
        

    if numberOfPlayer <= 2:
            print("You cannot be less than 2 players")
    elif numberOfPlayer in range(2,21):
            shuffler()

    elif numberOfPlayer > 20:
            print("You can't be more than 20 players")

except:
    print("Error.")