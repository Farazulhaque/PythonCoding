states = ['state1', 'state2', 'state3', 'state4', 'state5',
          'state6', 'state7', 'state8', 'state9', 'state10']
ask = input("Do you want to start a trip?[Y/n]: ")
visited_states = []
i = 1
if (ask.lower() == "y"):
    print(states)
    startstate = input("From which state, you want to start? ")
    while startstate not in states:
        startstate = input("From which state, you want to start? ")
    visited_states.append(startstate)

    while i < 10:
        next_state = input("Enter next state: ")
        while next_state not in states:
            print("Please enter states from available states.")
            next_state = input("Enter next state: ")
        visited_states.append(next_state)
        visit_more = input("Do you want to visit more?[Y/n]: ")
        if visit_more.lower() != 'y':
            break
        i += 1
else:
    exit(0)

print("Visited States: ", end="")
count = 0
for i in visited_states:
    if i not in visited_states[:count]:
        print(i, end=" ")
        count += 1

print(f"\nTotal states visited are: {count}")
