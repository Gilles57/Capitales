import os
import tools


def clear_screen():
    os.system("clear")


def menu(prompt, items):

    while True:

        print(prompt)
        for item in items:
            print(f'[{item[0]}] {item[1]}')

        choice = input("Option choisie ? ")
        for item in items:
            if choice == item[0]:
                clear_screen()
                return choice
        clear_screen()
        print("Choix erroné !")
