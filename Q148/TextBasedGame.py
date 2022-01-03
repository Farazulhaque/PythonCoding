# A dictionary for the simplified Realm of the Undead Arena Game
# The dictionary links a room to other rooms.
import sys

rooms = {
    'Living Room': {'West': 'Dining Room', 'North': 'Backyard', 'East': 'Bathroom', 'South': 'Study'},
    'Study': {'North': 'Living Room', 'East': 'Child Bedroom'},
    'Backyard': {'East': 'Graveyard', 'South': 'Living Room'},
    'Graveyard': {'West': 'Backyard'},
    'Child Bedroom': {'West': 'Study'},
    'Master Bedroom': {'South': 'Bathroom'},
    'Bathroom': {'West': 'Living Room', 'North': 'Master Bedroom'},
    'Dining Room': {'East': 'Living Room', 'South': 'Kitchen'},
    'Kitchen': {'North': 'Dining Room'},
}
items = {
    'Living Room': '',
    'Study': 'ReligiousText',
    'Graveyard': 'DemonName',
    'Child Bedroom': 'Villain',
    'Master Bedroom': 'HappyPicture',
    'Bathroom': 'HolyWater',
    'Dining Room': 'Candles',
    'Kitchen': 'Sage',
}
state = 'Living Room'
inventory = []


# function
def get_new_state(state, direction):
    new_state = state  # declaring
    for i in rooms:  # loop
        if i == state:  # if
            if direction in rooms[i]:  # if
                new_state = rooms[i][direction]  # assigning new_state

    return new_state  # return


while 1:  # gameplay loop
    print('You are in the ', state)  # printing state
    if state == 'Child Bedroom':
        print('Battling with the villain', end='')
        for i in range(50):
            for j in range(1000000):
                pass
            print(".", end='', flush=True)
        print()
        if len(inventory) == 6:
            print('You won - congratulations')
        else:
            print('Sorry, you lost - be better armed next time')
        break
    if(state != 'Living Room'):
        print('Available to you in this room is', items[state])
    print('You currently have', inventory)
    direction = input(
        'Enter item you want OR direction to go OR exit to give up: ')  # asking user
    if direction.lower() == items[state].lower():
        if items[state] not in inventory:
            inventory.append(items[state])
        continue
    # making first character capital remaining lower
    direction = direction.capitalize()
    if direction == 'Exit':  # if
        sys.exit(0)  # exit function
    if direction == 'East' or direction == 'West' or direction == 'North' or direction == 'South':  # if
        new_state = get_new_state(state, direction)  # calling function
        if new_state == state:  # if
            # print
            print(
                'There is a fearsome darkness in that direction quickly enter other direction!')
        else:
            state = new_state  # changing state value to new_state
    else:
        print('Invalid direction!!')  # print
