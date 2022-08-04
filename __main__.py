import sys
import csv
import random

import intro
import tools

items = [("1", "Jouer avec les pays d'Europe"),
         ("2", "Jouer avec tous les pays"),
         ("3", "Quitter le jeu")]

while True:
    choice = tools.menu("\nQue veux-tu faire ?", items)

    print(choice)

    match choice:
        case "1":
            file_of_states = "payscapitaleseurope.csv"

        case "2":
            file_of_states = "payscapitalesmonde.csv"

        case "3":
            sys.exit()

    nb_of_questions = 5

    nb = input("\nCombien veux-tu de questions ? (5 par défaut): ")
    if nb.isdigit():
        nb_of_questions = int(nb)

    states = []
    with open(file_of_states, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            states.append(row)

    score = 0

    questions = random.sample(states, nb_of_questions)
    for question in questions:

        response = input(f"Quelle est la capitale du pays suivant : {question['NOM']} ? ")

        if response == '':
            initiale = question['CAPITALE'][0]
            nb_of_caracters = len(question['CAPITALE']) - 1

            print(f"Voici un indice : {initiale} {'_ ' * nb_of_caracters}")
            response = input(f"Quelle est la capitale du pays suivant : {question['NOM']} ? ")
            if response.lower() == question['CAPITALE'].lower():
                score += 1
                print('Bonne réponse')
            else:
                print(f"Réponse erronée, c'était : {question['CAPITALE']}")

        elif response.lower() == question['CAPITALE'].lower():
            score += 2
            print('Bonne réponse')
        else:
            print(f"Réponse erronée, c'était : {question['CAPITALE']}")

    tools.clear_screen()
    nb_of_stars = len(f'Score : {score} sur {nb_of_questions * 2}')
    print('\n' + '*' * nb_of_stars)
    print(f"Score : {score} sur {nb_of_questions * 2}")
    print('*' * nb_of_stars)
