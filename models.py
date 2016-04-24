import os
import pickle

DEFAULT_FILENAME = "contact_list.txt"


class Contact(object):
    def __init__(self, filename=None):
        self.first_name = ""
        self.last_name = ""
        self.phone_number = ""
        if filename is None:
            filename = DEFAULT_FILENAME
        self.filename = filename
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                try:
                    loaded_dict = pickle.load(f)
                except pickle.UnpicklingError:
                    print "Invalid pickle file, loading failed"

            self.first_name = loaded_dict.get('first_name', '')
            self.last_name = loaded_dict.get('last_name', '')
            self.phone_number = loaded_dict.get('phone_number', '')

    def __str__(self):
        return "Full Name: {} {}\nPhone Number: {}".format(self.first_name, self.last_name, self.phone_number)

    def save(self):
        contact_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number,
        }
        with open(self.filename, 'w') as f:
            try:
                pickle.dump(contact_dict, f)
                print "Save Successful!"
            except pickle.PickleError:
                print "Cannot write to file"
