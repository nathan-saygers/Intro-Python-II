from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons", 'foyer', 'none', 'none', 'none'),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'overlook', 'outside', 'narrow', 'none'),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", 'none', 'foyer', 'none', 'none'),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'treasure', 'none', 'none', 'foyer'),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 'none', 'narrow', 'none', 'none'),
}

# Declare directions for input

directions = ('n', 's', 'e', 'w')

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

davie = Player('Davie Jones', 'outside')

print(room[davie.current_room])

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

player_input = input("Please enter a command:")

while player_input != 'q':
    print(room[davie.current_room])
    if player_input in directions:
        print('nice job choosing:', player_input)
        
        player_input = input("Please enter a command:")
    else:
        print('Please enter a cardinal direction (ex. n, s, e, w)')
        player_input = input("Please enter a command:")