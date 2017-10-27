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
            add_todo_item -- creates an instance of the class and add it to the task list'''

    def __init__(self):
        self.is_done = False

    def add_name(self):
        while True:
            try:
                system('clear')
                task_name = str(input("Please enter name of the task: "))
                if len(task_name) > 20 or len(task_name) < 1:
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
                    sys.exit()

    def add_description(self):
        while True:
            try:
                system('clear')
                task_description = str(input("Please enter description of the task: "))
                if len(task_description) > 150 or len(task_description) < 1:
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
                    sys.exit()

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
    
    def present_list():
        print_task_list(task_list.todo_list)

class DeleteItem(Controler):
    pass

class DisplayItem(Controler):
    pass

class MarkItemDone(Controler):
    pass

class ModifyItem(Controler):
    pass



    
