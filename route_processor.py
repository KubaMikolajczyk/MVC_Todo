from view import *
from controler import *
from data_model import *
import sys


def main():
    '''main loop of the program'''
    User.input_name()
    LoadFromFile.loading_file()

    while True:
        menu_option_choice = MenuChoice.choose_from_menu()

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
            SaveToFile.update_file()
            
        elif menu_option_choice == 8:
            sys.exit()

        elif menu_option_choice == 9:
            pass

if __name__ == "__main__":
    main()