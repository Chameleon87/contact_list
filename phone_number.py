#!usr/bin/env
"""
Contact App
"""
from models import Contact
from new_contact import new_contact_first_name

contact = Contact()


def start():
    print "Welcome to Contacts Plus!\n Would you like to take a look at all your contacts?"
    contacts_answer = raw_input().lower()
    if contacts_answer == "yes":
        print contact
    else:
        print "Would you like to add a contact?"
        b = raw_input().lower()
        if b == "yes":
            new_contact_first_name(contact)
        else:
            start()
start()
