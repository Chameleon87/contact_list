#!usr/bin/env
"""
Contact App
"""
import pickle

class Contact(object):
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.phone_number = ""

    def writing(self):
        new_contact()

    def reading(self):
        a = "contact_list.txt"
        x = pickle.load(open(a, 'r'))
        print x

c = Contact()

def start():
    print "Welcome to Contacts Plus!\n Would you like to take a look at all your contacts?"
    contacts_answer = raw_input().lower()
    if contacts_answer == "yes":
        print "Here is a list of all of your contacts saved so far:\n"
        c.reading()
    else:
        print "Would you like to add a contact?"
        b = raw_input().lower()
        if b == "yes":
            new_contact_first_name()
        else:
            start()


def new_contact_first_name():
    print "Please enter the first name of the contact you would like to add."
    c.first_name = raw_input().capitalize()
    print "Is " + c.first_name + " the correct first name?"
    first_name_answer = raw_input().lower()
    if first_name_answer == "yes":
        new_contact_last_name()
    else:
        new_contact_first_name()

def new_contact_last_name():
    print "What's the last name of the person you're attempting to add?"
    c.last_name = raw_input().capitalize()
    print "Is " + c.last_name + " the name you're attempting to add?"
    last_name_answer = raw_input().lower()
    if last_name_answer == "yes":
        new_contact_phone_number()


def new_contact_phone_number():
    a = "contact_list.txt"
    print "Please enter the phone number for the contact you are attempting to add."
    c.phone_number = raw_input().lower()
    if len(c.phone_number) < 10:
        print "please enter a phone number that contains 10 digits"
    else:
        NewContact = {c.first_name + ' ' + c.last_name: c.phone_number}
        print NewContact
        pickle.dump(NewContact, open(a, 'w'))
        print "Save Successful!"

start()
