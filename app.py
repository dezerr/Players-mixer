import random
import os

try:

    os.system("cls")
    os.system("color c")


    print("-----------------------------")
    print("Tool made by dezerr")
    print("-----------------------------\n")
    numberOfPlayer = input("Quels est le nombre de joueurs ? : ")
    numberOfPlayer = int(numberOfPlayer)
    

    def shuffler():
        i = 0
        iPlusOne = i + 1
        # Tableau qui contient tous les joueurs
        arrNameOfPLayer = []

        while i < numberOfPlayer:
            nameOfPlayer = input("Quel est le nom du joueur " + str(iPlusOne)  + " ? : ")
            arrNameOfPLayer.append(nameOfPlayer)
            i = i + 1
            iPlusOne = iPlusOne + 1

        print("\nLes joueurs sont : " + str(arrNameOfPLayer))
        random.shuffle(arrNameOfPLayer)
        print("\nLes joueurs ont été mélanger aléatoirement : " + str(arrNameOfPLayer) + "\n")


        # Séparation d'équipes
        numberOfTeam = input("Combien d’équipes voulez vous ? : ")
        numberOfTeam = int(numberOfTeam)
        test = numberOfPlayer % numberOfTeam

        if test == 0:
            pad = len(arrNameOfPLayer) / numberOfTeam
            pad = int(pad)
            aS = [arrNameOfPLayer[i:i+pad]for i in range(0, len(arrNameOfPLayer) - pad + 1, pad)]
            print("Voici les " + str(numberOfTeam) + " équipes : \n")
            print(aS)
            print("\n")
        else:
            print("Ce n'est pas possible")
        

    if numberOfPlayer <= 2:
            print("Vous ne pouvez pas être moin de 2 joueur")
    elif numberOfPlayer in range(2,21):
            shuffler()

    elif numberOfPlayer > 20:
            print("Vous ne pouvez pas être plus de 20 joueurs")

except:
    print("Erreur.")