# declaration
rooms = {
    'Isla Blanquilla': {'South': 'Cumana', 'East': 'Grenada', 'West': 'Curacao', 'North': 'St. Kitts', 'item': ""},
    'Curacao': {'East': 'Isla Blanquilla', 'item': 'Cutlass'},
    'Grenada': {'West': 'Isla Blanquilla', 'North': 'Barbados', 'item': 'Cannons'},
    'Barbados': {'South': 'Grenada', 'item': 'Kracken'},  # VILLAIN
    'St. Kitts': {'South': 'Isla Blanquilla', 'East': 'Antigua', 'item': 'Crew'},
    'Antigua': {'West': 'St. Kitts', 'item': 'Frigate'},
    'Cumana': {'North': 'Isla Blanquilla', 'East': 'Trinidad', 'item': 'Gold Doubloons'},
    'Trinidad': {'West': 'Cumana', 'item': 'Rum'}
}
state = 'Isla Blanquilla'


# function
def get_new_state(state, direction):
    new_state = state  # declaraing
    for i in rooms:  # loop
        if i == state:  # if
            if direction in rooms[i]:  # if
                new_state = rooms[i][direction]  # assigning new_state
    return new_state  # return


# function
def get_item(state):
    return rooms[state]['item']  # returning Item value


# function
def show_instructions():
    # print a main menu and commands
    print('Pirate Text Adventure Game')
    print('Collect 6 items to win the game, or fail your mission.')
    print('Move commands: go South, go North, go East, go West')
    print("Add to Inventory: get 'item name'")


show_instructions()  # calling function
inventory = []
while (1):  # gameplay loop
    print('You are in ', state)  # printing state
    print('Inventory:', inventory)  # printing inventory
    item = get_item(state)  # calling get_item function
    if item not in inventory:
        print('You see a', item)  # print
    print('------------------------------')
    if item == 'Kracken' and len(inventory) != 6:  # if
        print('NOM NOM...GAME OVER!')
        print('Thanks for playing! Hope you enjoyed it!')
        exit(0)
    if item == 'Kracken' and len(inventory) == 6:
        # print
        print('Congratulations! You have collected all items and defeated the Kracken!')
        print('Thanks for playing! Hope you enjoyed it!')
        exit(0)
    direction = input('Enter your move: ').title()  # asking user
    if (direction == 'Go East' or direction == 'Go West' or direction == 'Go North' or direction == 'Go South'):  # if
        direction = direction[3:]
        new_state = get_new_state(state, direction)  # calling function
        if new_state == state:  # if
            print('The room has wall in that direction enter other direction!')  # print
        else:
            state = new_state  # changing state value to new_state
    elif direction == str('Get '+item):  # if
        if item in inventory:  # if item already present in inventory
            print('Item already taken go to another room!!')
        else:
            print(f"{item} retrieved!\n")
            inventory.append(item)  # appending
    else:
        print('Invalid direction!!')  # print
