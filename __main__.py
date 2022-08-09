import sys

import intro
import tools
import game_engine

items = [("1", "Jouer avec les pays d'Europe"),
         ("2", "Jouer avec tous les pays"),
         ("3", "Quitter le jeu")]

while True:
    choice = tools.menu("\nQue veux-tu faire ?", items)

    print(choice)

    match choice:
        case "1":
            game_engine.game("payscapitaleseurope.csv")

        case "2":
            game_engine.game("payscapitalesmonde.csv")

        case "3":
            sys.exit()


