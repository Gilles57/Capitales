import csv
import random
import tools


def game(file_of_states):
    nb_of_questions = 3
    players = []

    nb_of_players = input("\nCombien y a-t-il de joueurs ? (1 par défaut) : ")
    if nb_of_players.isdigit():
        nb_of_players = int(nb_of_players)
    else:
        nb_of_players = 1

    for i in range(nb_of_players):
        name = input(f"Joueur n° {i + 1}, quel est ton nom ? ")
        players.append({'name': name, 'score': 0})

    for player in players:
        score = 0
        print(f"{player['name']}, à toi de jouer !\n")

        states = []
        with open(file_of_states, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                states.append(row)

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

        player['score'] = score

    results = sorted(players,key=lambda  d: d['score'], reverse = True)
    print("\n**** CLASSEMENT ****")
    for result in results:
        print(f"{result['name']} : {result['score']}")
