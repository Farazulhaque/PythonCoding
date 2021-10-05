print("Zombie Invasion Text Game")
print("Collect 6 items to win the game, or be eaten by the Zombie.")
print("Move commands: go South, go North, go East, go West")
print("Add to Inventory: get 'item name'")
rooms = {
   'Bedroom 1': {'South': 'Kitchen', 'East': 'Bathroom 1'},
   'Bathroom 1': {'West': 'Bedroom 1', 'item': 'Hammer'},
   'Kitchen': {'West': 'Living Room', 'East': 'Bedroom 2', 'South': 'Dining Room', 'North': 'Bedroom 1', 'item': 'Smoke Bomb'},
   'Living Room': {'East': 'Kitchen', 'item': 'Loaded Gun'},
'Dining Room': {'North': 'Kitchen', 'East': 'Garage', 'item': 'Gas Mask'},
   'Bedroom 2': {'West': 'Kitchen', 'North': 'Bathroom 2', 'item': 'Nails'},
   'Bathroom 2': {'South': 'Bedroom 2', 'item': 'Wood'},
   'Garage': {'West': 'Dining Room', 'item': 'Zombie!!'}
}
position = "Start"
print("You are in Bedroom 1")
while True:
    direction = input(
        "Please enter direction to move (East/West/North/South) or Q to quit: ").upper()
    if direction == "Q":
        break
    if direction in paths[position]:
        print("You have reached the " + paths[position][direction])
    position = paths[position][direction]
    print("You now have available to you: " + objects[position])
    if position == "Garage":
        time.sleep(3)
        print("You killed the zombie and fixed the door!")
        break
    else:
        print("\nSorry, no path in that direction!")
