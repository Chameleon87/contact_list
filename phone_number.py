#!usr/bin/env
"""
Contact App
"""
import os
import pickle
#local imports
from models import Contact
from new_contact import new_contact_first_name, new_contact_last_name, new_contact_phone_number

c = Contact()

def start():
    print "Welcome to Contacts Plus!\n Would you like to take a look at all your contacts?"
    contacts_answer = raw_input().lower()
    if contacts_answer == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        print "Here is a list of all of your contacts saved so far:"
        c.reading()
    else:
        print "Would you like to add a contact?"
        b = raw_input().lower()
        if b == "yes":
            new_contact_first_name()
        else:
            start()
start()
