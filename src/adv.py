from room import Room
from player import Player
#  from item import Item
from item import all_items


# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'secret': Room("Secret Room", "Your greediness has led to your demise. Deep in the secret room youll find a "
                                  "surprise"),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].n_to = room['secret']

# Link items to rooms
room['outside'].item_list = [all_items['armor']]
room['foyer'].item_list = [all_items['helmet']]
room['overlook'].item_list = [all_items['spear']]
room['narrow'].item_list = [all_items['diamond']]
room['treasure'].item_list = [all_items['gold']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
# p = Player("Test Player", room['outside'], "outside", "desc", 'n_to', 's_to', 'e_to', 'w_to')
p = Player("Test Player", room['outside'])

play = input('Would you like to play a game? (y/n): ')
if play == "y":
    print('great!')
elif play == "n":
    print('too bad!')
else:
    print('invalid answer')

# Write a loop that:
while play == "y":  # * Prints the current room name # * Prints the current description
    move = input(f'{p.name}, you are currently at the {p.current_location}\n'
                 f'There is{p.current_location.item_list}'
                 f' in the room\nWhere would you '
                 f'like to go? Options(n, s, e, w, '
                 f'get, take, drop, i'
                 '\nAction: ').split(' ')
    print(move)
    for key in all_items:
        key

    if move[0] in ("n", "e", "s", "w"):
        new_room = getattr(p.current_location, f'{move[0]}_to')
        if new_room is None:
            print("cannot go that way")
        else:
            p.current_location = new_room

    elif move[0] and move[1]:
        print("move 0", move[0])
        print("move 1", move[1])
        print("current location item list", p.current_location.item_list)
        if move[0] == "get" and move[1]:
            p.current_inventory.append(p.current_location.item_list.pop())
            print("current inventory", p.current_inventory)
        elif move == "take":
            pass
        elif move[0] == "drop" and move[1]:
            p.current_location.item_list.append(p.current_inventory.pop())

        elif move[0] == "open" and move[1] == "i":
            print("open i", p.current_inventory)

    else:
        print("invalid command")

"""
    if p.current_inventory is None:
        print("You have no items")
    else:
        print(p.current_inventory)

    if move == "n":
        if p.current_location.n_to is None:
            print("you cannot go that way from here")
        else:
            p.current_location = p.current_location.n_to

    elif move == "e":
        if p.current_location.e_to is None:
            print("you cannot go that way from here")
        else:
            p.current_location = p.current_location.e_to

    elif move == "s":
        if p.current_location.s_to is None:
            print("you cannot go that way from here")
        else:
            p.current_location = p.current_location.s_to

    elif move == "w":
        if p.current_location.w_to is None:
            print("you cannot go that way from here")
        else:
            p.current_location = p.current_location.w_to

    elif move == "q":  # If the user enters "q", quit the game.
        exit()

    else:
        print("that is not a valid command. TRY AGAIN!!")
"""
# * Waits for user input and decides what to do.


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
