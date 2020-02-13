# Implement a class to hold room information. This should have name and
# description attributes
# should be around 15 lines of code
from item import Item


class Room:
    def __init__(self, name, description, n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.item_list = []

    def search_room(self):
        # return items located in room (current_room?)
        pass

    def __str__(self):
        return f'{self.name}, {self.description}'


