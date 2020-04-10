from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

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
}

items = {
    'torch': Item('torch', 'a simple torch'),
    'sword': Item('sword', 'such a very sharp sword')
}

# Link rooms together

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

# Place room items

room['foyer'].items = [items['torch'], items['sword']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

davie = Player('Davie Jones', 'outside')

# print(room['foyer'].items)

# print(room[davie.current_room].n_to)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Loop helpers:

print(room[davie.current_room])
player_input = input("Please enter a command:")

def move():
    global player_input
    move_dir = f"{player_input}_to"
    if getattr(room[davie.current_room], move_dir) != None:
        davie.current_room = getattr(room[davie.current_room], move_dir)
        print(room[davie.current_room])
        room[davie.current_room].print_items()
        player_input = input("Please enter a command:")
    else:
        print('There is no room in that direction')
        player_input = input("Please enter a command:")

# def get():


# REPL:

while player_input != 'q':
    input_arr = player_input.split(" ")
    if len(input_arr) < 2:
        if player_input == 'n' or player_input == 's' or player_input == 'e' or player_input == 'w':
            move()
        elif player_input == 'i':
            davie.print_inventory()
            player_input = input("Please enter a command:")
        else:
            print('Please enter a cardinal direction (ex. n, s, e, w)')
            player_input = input("Please enter a command:")
    else:
        if input_arr[0] == 'get':
            if room[davie.current_room].got_item(input_arr[1]):
                davie.get_item(items[input_arr[1]])
                print(f"You picked up the {input_arr[1]}")
                player_input = input("Please enter a command:")
            else: 
                print(f"There is no {input_arr[1]} in this room ya goober")
                player_input = input("Please enter a command:")
        elif input_arr[0] == 'drop':
            if davie.dropped_item(input_arr[1]):
                room[davie.current_room].receive_item(items[input_arr[1]])
                print(f"You dropped the {input_arr[1]}")
                player_input = input("Please enter a command:")
            else: 
                print(f"You don't have a {input_arr[1]} to drop!")
                player_input = input("Please enter a command:")
        else:
            print('Please enter a valid two word command (ex. get torch, drop drawers)')
            player_input = input("Please enter a command:")