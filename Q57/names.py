def main():
    filename = "names.txt"
    # To store names stored in names.txt in names list
    names = []
    # Open file to read
    with open(filename, "r") as file:
        # Loop over each line
        for name in file:
            # Added each line into list by removing newline character("\n") from each line
            names.append(name.rstrip("\n"))

    # User input for searching name
    search_name = input("Enter a first name to search for: ")
    # Initially namefound is false
    nameFound = False
    # Loop over list to search for user input name
    for i in names:
        # Check if name in list
        if i == search_name:
            # set name found to true
            nameFound = True
            # Print name found
            print("Name Found")
            # And exit the loop
            break
    # If still namefound is equal to false means name is not in the list
    if nameFound == False:
        print("Name not found")

    # Sort the names
    names.sort()
    # Open sorted_names.txt in append mode to add sorted names
    with open("sorted_names.txt", "a") as sorted_file:
        # Loop over each names
        for name in names:
            # Add name to sorted_names.txt and also "\n" for newline
            sorted_file.write(name)
            sorted_file.write("\n")


# Calling main()
main()
