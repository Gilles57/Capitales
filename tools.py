import os
import tools


def clear_screen():
    os.system("clear")


def menu(prompt, items):

    while True:

        print(prompt)
        for item in items:
            print(f'[{item[0]}] {item[1]}')

        choice = input("Quel est ton choix ? ")
        for item in items:
            if choice == item[0]:
                tools.clear_screen()
                return choice
        tools.clear_screen()
        print("Choix erroné !")
