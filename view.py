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


def print_task_list(task_list):
    '''present task list in order that they were added'''

    clean_screen()
    if task_list == []:
        print('''
        You have no task at the moment
        Add more if you wish!''')
    else:
        index = 1
        for element in task_list:
            print(str(index) + ". " + element.__str__())
            index += 1

    input("\n\nPush any button to continue...")


def clean_screen():
    os.system('clear')