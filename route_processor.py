from view import *
from controler import *
import sys


def main():
    '''main loop of the program'''
    welcome_message()
    while True:
        menu_option_choice = print_menu()

        if menu_option_choice == 1:
            AddItem.add_todo_item()

        elif menu_option_choice == 2:
            DisplayList.present_list()

        elif menu_option_choice == 3:
            DeleteItem.choose_task_to_delete()

        elif menu_option_choice == 4:
            pass

        elif menu_option_choice == 5:
            pass

        elif menu_option_choice == 6:
            pass
            
        elif menu_option_choice == 7:
            sys.exit()

if __name__ == "__main__":
    main()