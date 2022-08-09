import csv
import random
import tools


def game(file_of_states):
    nb_of_questions = 5

    # nb = input("\nCombien veux-tu de questions ? (5 par défaut): ")
    # if nb.isdigit():
    #     nb_of_questions = int(nb)

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
            nb_of_characters = len(question['CAPITALE']) - 1

            print(f"Voici un indice : {initiale} {'_ ' * nb_of_characters}")
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
