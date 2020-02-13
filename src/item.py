"""
Create a file called item.py and add an Item class in there.
The item should have name and description attributes.
Hint: the name should be one word for ease in parsing later.
This will be the base class for specialized item types to be declared later.
"""


class Item:
    def __init__(self, item_name, item_desc):
        self.item_name = item_name
        self.item_desc = item_desc

    # add on_take method to Item # call this method when Item is picked up by player
    def on_take(self):
        # print You have picked up [NAME] when you pick up an item
        print(f'You have picked up {self.item_name}')
        # the Item can use this to run additional code when its picked up

    # add an on_drop method to Item
    def on_drop(self):
        # implement this similar to on_take
        print(f'You dropped {self.item_name}')

    def __str__(self):
        return f'{self.item_name}, {self.item_desc}'


all_items = {
    'sword': Item("Sword", "The sword hums with a strange power."),
    'helmet': Item("Helmet", "The most uninteresting helmet you've ever laid eyes upon."),
    'shield': Item("Shield", "The greatest offense is a good defense."),
    'chest': Item("Chest", "This chest contains the grand gift of knowledge."),
    'armor': Item("Armor", "Protects you from bad people."),
    'spear': Item("Spear", "Sharp ends on this weapon."),
    'gold': Item("Gold", "A pile of pure gold."),
    'diamond': Item("Diamond", "A sharp perfectly cut diamond."),
    'ruby': Item("Ruby", "A beautiful stone, red as blood."),
    'emerald': Item("Emerald", "A beautiful stone, green as a grass."),
}
