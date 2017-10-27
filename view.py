from user_controler import *
import os


def welcome_message():
    clean_screen()
    print("Hello Welcome to MVC Todo app :)")
    name = input_name()
    clean_screen()
    print("Welcome " + str(name) + ".")


def clean_screen():
    os.system('clear')