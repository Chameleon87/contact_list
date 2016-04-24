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
