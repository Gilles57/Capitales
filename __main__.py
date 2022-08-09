import sys

import intro
import tools
import game_engine


items = [("1", "Jouer avec les pays d'Europe"),
         ("2", "Jouer avec tous les pays"),
         ("3", "Quitter le jeu")]

while True:
    # if nb_of_players == 1:
    choice = tools.menu("\nQue veux-tu faire ?", items)
    # else:
    #     choice = tools.menu("\nQue voulez-vous faire ?", items)


   #  print(choice)

    match choice:
        case "1":
            game_engine.game("payscapitaleseurope.csv")

        case "2":
            game_engine.game("payscapitalesmonde.csv")

        case "3":
            sys.exit()


