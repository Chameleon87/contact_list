import os
import pickle

a = "contact_list.txt"

class Contact(object):
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.phone_number = ""

    def reading(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print "Here is a list of all of your contacts saved so far:"
        x = pickle.load(open(a, 'r'))
        print x

    def writing(self):
        self.reading()
        new_contact = {self.first_name + ' ' + self.last_name: self.phone_number}
        new_dic = new_contact + self.reading()
        print new_dic
        pickle.dump(new_dic, open(a, 'wb'))
        print "Save Successful!"


