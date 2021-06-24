def filter_all_num_strings(list_of_str):
    List = []
    # Iterate over all the elements of list
    for i in list_of_str:
        # Iterate over each letter of elements
        for j in i:
            if j in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                List.append(i)
                # If number in a word then append the word to a list and break this loop
                break
    return List


my_los = ["ICS3U", "MCV4U", "Visual Art", "VLC",
          "MPM1D", "88Average", "internet", "Covid-19"]

print(filter_all_num_strings(my_los))

# Output
# ['ICS3U', 'MCV4U', 'MPM1D', '88Average', 'Covid-19']