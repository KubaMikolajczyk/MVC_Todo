import sys
from data_model import *
from error_handling import *
from os import system
from view import *


class Controler(object):
    '''Base class for controlers in this module.'''
    pass


class AddItem(Controler):
    '''Creation class for each task in todo task list
        
        Functions:
            add_name -- creates string name within the lenght of 20 letters
            add_description -- creates string description up to the lenght of 150 letters
            add_todo_item -- creates an instance of the class and add it to the task list
            check_if_in_task_list -- used by other classes to check if instance is part of task list
            __str__ -- format the way each item will be presented in list'''

    def __init__(self):
        self.is_done = False

    def add_name(self):
        max_len = 20
        min_len = 1

        while True:
            try:
                system('clear')
                task_name = str(input("Please enter name of the task: "))
                if len(task_name) > max_len or len(task_name) < min_len:
                    raise LenghtError("This string is not required lenght")
                self.task_name = task_name
                break

            except LenghtError:
                decide_if_continue = input('''
                Name of the task should be at least one letter long
                but can't be longer than 20 letters. 
                
                Do you wish to continue? [Y/N]:''')
                if decide_if_continue.upper() == "Y":
                    continue
                else:
                    break

    def add_description(self):
        max_len = 150
        min_len = 1

        while True:
            try:
                system('clear')
                task_description = str(input("Please enter description of the task: "))
                if len(task_description) > max_len or len(task_description) < min_len:
                    raise LenghtError("This string is not required lenght")
                self.task_description = task_description
                break

            except LenghtError:
                decide_if_continue = input('''
                Description of the task should be at least one letter long
                but can't be longer than 150 letters. 
                
                Do you wish to continue? [Y/N]:''')
                if decide_if_continue.upper() == "Y":
                    continue
                else:
                    break

    def __str__(self):
        if self.is_done:
            return "[x] -- " + self.task_name
        else:
            return "[ ] -- " + self.task_name

    def check_if_in_task_list(self):
        return True
    
    @staticmethod
    def add_todo_item():
        new_item = AddItem()
        new_item.add_name()
        new_item.add_description()
        task_list.todo_list.append(new_item)
        new_task_msg()

    
class DisplayList(Controler):
    '''connect with data_model to gather actual list and pass it to view.print_task_list'''

    @staticmethod
    def present_list():
        print_task_list(task_list.todo_list)


class DeleteItem(Controler):
    '''reach to data_model to gather actual list and delete an item by index'''

    @staticmethod
    def choose_task_to_delete():
        adjust_index_to_list = 1

        if task_list.todo_list == []:
            empty_task_list_msg()
        else:

            while True:

                try:
                    system('clear')
                    task_index = int(input('Please enter index of a task you want to delete: '))
                    try:
                        task_list.todo_list.pop((task_index - adjust_index_to_list))
                        remove_task_msg()
                        break

                    except IndexError:
                        decide_if_continue = input('''
                            The task that you just selected does not exist
                            to see all actual tasks go back to menu
                            and choose option '2'.
                            
                            Do you wish to continue operation? [Y/N]:''')
                        if decide_if_continue.upper() == "Y":
                            continue
                        else:
                            break

                except ValueError:
                    decide_if_continue = input('''
                    Index of an item should be an integer
                    if you want to see the list go back to menu
                    and choose option '2'.

                    Do you want to continue operation? [Y/N]:''')
                    if decide_if_continue.upper() == "Y":
                        continue
                    else:
                        break


class DisplayItem(Controler):
    '''reaches for data_model.todo_list to select specific task by index and process it to view'''

    @staticmethod
    def select_item_to_display():
        adjust_index_to_list = 1

        if task_list.todo_list == []:
            empty_task_list_msg()
        else:

            while True:

                try:
                    system('clear')
                    task_index = int(input('Please enter index of a task you want to see: '))
                    print_specific_task(task_list.todo_list, task_index)
                    break

                except ValueError:
                    decide_if_continue = input('''
                    Index of an item should be an integer
                    if you want to see the list go back to menu
                    and choose option '2'.

                    Do you want to continue operation? [Y/N]:''')
                    if decide_if_continue.upper() == "Y":
                        continue
                    else:
                        break


class MarkItemDone(Controler):
    '''reaches for data_model.todo_list to mark specific task as done'''

    @staticmethod
    def select_task_done():
        adjust_index_to_list = 1

        if task_list.todo_list == []:
            empty_task_list_msg()
        else:

            while True:
                
                try:
                    system('clear')
                    task_index = int(input('Please enter index of a task you want to mark as done: '))
                    
                    try:
                        task_list.todo_list[(task_index - adjust_index_to_list)].is_done = True
                        mark_done_msg()
                        break

                    except IndexError:
                        decide_if_continue = input('''
                            The task that you just selected does not exist
                            to see all actual tasks go back to menu
                            and choose option '2'.
                            
                            Do you wish to continue operation? [Y/N]:''')
                        if decide_if_continue.upper() == "Y":
                            continue
                        else:
                            break

                except ValueError:
                    decide_if_continue = input('''
                    Index of an item should be an integer
                    if you want to see the list go back to menu
                    and choose option '2'.

                    Do you want to continue operation? [Y/N]:''')
                    if decide_if_continue.upper() == "Y":
                        continue
                    else:
                        break


class ModifyItem(Controler):
    '''reaches for data_model.todo_list to select specified task
    
    Functions:
        edit_name -- asks user to enter new name if wanted
        edit_description -- asks user to enter new description if wanted
        modify_specified_task -- perform functions above after specified task selection by index
    '''

    @staticmethod
    def edit_name(task_index, adjust_index_to_list):
        max_len = 20
        min_len = 1

        system('clear')
        name_edition_choice = input('Do you want to edit name of the task? [Y/N]')
        if name_edition_choice.upper() == 'Y':

            while True:

                try:
                    system('clear')
                    new_task_name = input('Please enter new name for the task: ')
                    if len(new_task_name) > max_len or len(new_task_name) < min_len:
                            raise LenghtError("This string is not required lenght")
                    task_list.todo_list[(task_index - adjust_index_to_list)].task_name = new_task_name
                    break

                except LenghtError:
                    decide_if_continue = input('''
                    Name of the task should be at least one letter long
                    but can't be longer than 20 letters. 
                    
                    Do you wish to continue? [Y/N]:''')
                    if decide_if_continue.upper() == "Y":
                        continue
                    else:
                        break

    @staticmethod
    def edit_description(task_index, adjust_index_to_list):
        max_len = 150
        min_len = 1

        system('clear')
        description_edition_choice = input('Do you want to edit description of the task? [Y/N]')
        if description_edition_choice.upper() == 'Y':
            while True:

                try:
                    system('clear')
                    new_task_description = input('Please enter new description for the task: ')
                    if len(new_task_description) > max_len or len(new_task_description) < min_len:
                            raise LenghtError("This string is not required lenght")
                    task_list.todo_list[(task_index - adjust_index_to_list)].task_description = new_task_description
                    break

                except LenghtError:
                    decide_if_continue = input('''
                    Description of the task should be at least one letter long
                    but can't be longer than 150 letters. 
                    
                    Do you wish to continue? [Y/N]:''')
                    if decide_if_continue.upper() == "Y":
                        continue
                    else:
                        break

    @staticmethod
    def modify_specified_task():
        adjust_index_to_list = 1

        if task_list.todo_list == []:
            empty_task_list_msg()
        else:

            while True:

                try:
                    system('clear')
                    task_index = int(input('Please enter index of a task you want to modify: '))

                    try:
                        if task_list.todo_list[(task_index - adjust_index_to_list)].check_if_in_task_list():
                            pass

                    except IndexError:
                        decide_if_continue = input('''
                            The task that you just selected does not exist
                            to see all actual tasks go back to menu
                            and choose option '2'.
                            
                            Do you wish to continue operation? [Y/N]:''')
                        if decide_if_continue.upper() == "Y":
                            continue
                        else:
                            break

                    ModifyItem.edit_name(task_index, adjust_index_to_list)
                    ModifyItem.edit_description(task_index, adjust_index_to_list)
                    edit_done_msg()
                    break

                except ValueError:
                    decide_if_continue = input('''
                    Index of an item should be an integer
                    if you want to see the list go back to menu
                    and choose option '2'.

                    Do you want to continue operation? [Y/N]:''')
                    if decide_if_continue.upper() == "Y":
                        continue
                    else:
                        break


class User(Controler):

    def input_name():
        '''Call function to print an intro screen and pass the input name to welcome user'''

        intro_screen()
        name = input("\nCan you please enter your name: ")
        if name == '':
            name = 'User'
        personalized_welcome_message(name)


class MenuChoice(Controler):

    @staticmethod
    def choose_from_menu():

        time.sleep(1)

        while True:

            try:
                clean_screen()
                menu_choice = int(input('''
                You can choose from:
                1. Add new task
                2. Show all tasks
                3. Remove task
                4. Display specific task
                5. Mark task as done
                6. Modify task
                7. Save the task list
                8. Exit program

                '''))
                return menu_choice
            except ValueError:
                print("Im sorry but you have to choose a number. Try again.")
                time.sleep(2)