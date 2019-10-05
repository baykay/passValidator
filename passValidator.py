#!/usr/bin/python3
from termcolor import colored
import re

passwd = input(colored("[+] Enter password: ", 'green'))


def length():
    if len(passwd) > 8:
        isCaps()
    else:
        print(colored("Must be greater than 8 digits!", 'red'))


def specialChar():
    print(colored("Go to next step", 'yellow'))


def isCaps():
    if not passwd[0].isupper():
        print(colored("Must start with uppercase!", 'red'))
    else:
        containsNum()


def containsNum():
    if not passwd.isalnum():
        print(colored("Must contain a number and a special character!", 'red'))
    else:
        specialChar()  


# while passwd != 'q':
length()