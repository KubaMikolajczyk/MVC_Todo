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


def remove_task_msg():
    '''inform the user about controler.delete_task succesfull operation'''

    clean_screen()
    print('Task was deleted from the list! ')
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
            print("\n" + str(index) + ". " + element.__str__())
            index += 1

    input("\n\nPush any button to continue...")


def print_specific_task(task_list, task_index):
    '''present specific task using index provided by user
    
    index -- starting index in list iteration
    adjust_index_to_list -- additional variable to deal with diffrences between ui and lists
    adjust_index_to_format -- additional variable to prepare our index for formating for ui
    '''

    index = 0
    adjust_index_to_list = 1
    adjust_index_to_format = 1
    
    clean_screen()
    for element in task_list:
        if index == (task_index - adjust_index_to_list):
            print('\n' + str(index + adjust_index_to_format) + ". " + element.__str__() \
            + ' (' + element.task_description + ')')
        else:
            index += 1
    input("\n\nPush any button to continue...")


def mark_done_msg():
    '''inform the user about controler.mark_done_task succesfull operation'''

    clean_screen()
    print('Task you selected is now marked as done! :)')
    time.sleep(2)


def edit_done_msg():
    '''inform the user about controler.modify_specified_task succesful operation'''

    clean_screen()
    print('Task you chose was succesfully edit!')
    time.sleep(2)


def clean_screen():
    '''additional function for easier maintining terminal cleaning'''
    os.system('clear')
