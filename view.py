import os
import time


def intro_screen():
    '''inform user about the version of program and show welcome screen'''

    clean_screen()
    print('''
                   ,     :     ,
              '.    ;    :    ;    ,`
          '-.   '.   ;   :   ;   ,`   ,-`
       "-.   '-.  '.  ;  :  ;  ,`  ,-`   ,-"
          "-.   '-. '. ; : ; ,` ,-`   ,-"
     '"--.   '"-.  '-.'  '  `.-`  ,-"`   ,--"`
          '"--.  '"-.   ...   ,-"`  ,--"`
               '"--.  .:::::.  ,--"`
    ------------------:::::::--------------------
                       ~~~~~
                        ~~~
                         ~

        Welcome to MVC Todo project app 1.13

    ''')
    input('\n Press any button to continue...')


def personalized_welcome_message(name):
    '''recieves name and print it to the screen'''

    clean_screen()
    print("Welcome " + str(name) + ".")
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


def empty_task_list_msg():
    '''inform user when he try to operate on empty task list'''

    clean_screen()
    print('''
    You have no task at the moment
    Add more if you wish!''')
    input('\nPush any button to continue..')


def empty_task_list_creation_msg():
    '''inform user that new empty task list will be created'''

    clean_screen()
    print('''
    There will be new empty task list created for you!''')
    input('\nPush any button to continue..')


def file_not_found_msg(file_name):
    '''inform user about incorrectly inputed name of file'''

    if file_name == "":
        file_name = "'blank'"
    clean_screen()
    print('''
    Unfortunatelly there is no such file as {0}

    There will be new empty task list created for you!'''.format(file_name))
    input('\nPush any button to continue..')
