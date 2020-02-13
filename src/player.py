# Write a class to hold player information, e.g. what room they are in
# currently.
# can be done in 4 ish lines of code


class Player:
    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location

    def __str__(self):
        return f'{self.name}, your current location is {self.current_location}'



