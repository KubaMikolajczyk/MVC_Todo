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
                Name of the task should be at least one letter long
                but can't be longer than 150 letters. 
                
                Do you wish to continue? [Y/N]:''')
                if decide_if_continue.upper() == "Y":
                    continue
                else:
                    break

    def __str__(self):
        if self.is_done:
            return "[x] -- " + self.task_name + " (" + self.task_description + ")\n"
        else:
            return "[ ] -- " + self.task_name + " (" + self.task_description + ")\n"

    def add_todo_item():
        new_item = AddItem()
        new_item.add_name()
        new_item.add_description()
        task_list.todo_list.append(new_item)
        new_task_msg()

    
class DisplayList(Controler):
    '''connect with data_model to gather actual list and pass it to view.print_task_list'''

    def present_list():
        print_task_list(task_list.todo_list)


class DeleteItem(Controler):

    def choose_task_to_delete():
        adjust_index_to_list = 1

        while True:
            try:
                system('clear')
                task_index = int(input('Please enter index of a task you want to delete: '))
                task_list.todo_list.pop((task_index - adjust_index_to_list))
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
    pass

class MarkItemDone(Controler):
    pass

class ModifyItem(Controler):
    pass



    
