from user_controler import *
import os
import time


def welcome_message():
    '''recieves name and print it to the screen'''

    clean_screen()
    print("Hello Welcome to MVC Todo app :)")
    name = input_name()
    clean_screen()
    print("Welcome " + str(name) + ".")


def print_menu():
    '''showing all aviable features to the user'''

    time.sleep(1)
    while True:
        try:
            clean_screen()
            menu_choice = int(input('''
            MVC ToDo App 1.0
            
            You can choose from:
            1. Add new task
            2. Show all tasks
            3. Remove task
            4. Display specific task
            5. Mark task as done
            6. Modify task
            7. Exit program'''))
            return menu_choice
        except ValueError:
            print("Im sorry but you have to choose a number. Try again.")
            time.sleep(1)


def new_task_msg():
    '''reports when controler.add_task will be succesfully completed'''
    clean_screen()
    print('Task was added succesfully! :)')
    time.sleep(2)


def clean_screen():
    os.system('clear')