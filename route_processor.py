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
            DisplayItem.select_item_to_display()

        elif menu_option_choice == 5:
            MarkItemDone.select_task_done()

        elif menu_option_choice == 6:
            ModifyItem.modify_specified_task()
            
        elif menu_option_choice == 7:
            sys.exit()

if __name__ == "__main__":
    main()