def new_contact_first_name(c):
    print "Please enter the first name of the contact you would like to add."
    c.first_name = raw_input().capitalize()
    print "Is " + c.first_name + " the correct first name?"
    first_name_answer = raw_input().lower()
    if first_name_answer == "yes":
        new_contact_last_name(c)
    else:
        new_contact_first_name(c)


def new_contact_last_name(c):
    print "What's the last name of the person you're attempting to add?"
    c.last_name = raw_input().capitalize()
    print "Is " + c.last_name + " the name you're attempting to add?"
    last_name_answer = raw_input().lower()
    if last_name_answer == "yes":
        new_contact_phone_number(c)
    else:
        new_contact_last_name(c)


def new_contact_phone_number(c):
    print "Please enter the phone number for the contact you are attempting to add."
    c.phone_number = raw_input().lower()
    if len(c.phone_number) < 10:
        print "please enter a phone number that contains 10 digits"
    else:
        c.save()
