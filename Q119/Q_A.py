question = "Name something a baby does that would be unacceptable in a roommate"
possible_answers = [("CRY/AT 3 A.M", 39), ('POO/WET SELF', 28), ("PUKE/ON ME", 9), ("BURP", 8),
                    ("MAKE MESS/TOSS FOOD", 5), ("FART", 4), ("PEE/IN MY FACE", 3), ("NURSE/ON MY NIPS", 2)]

player_strikes_left = 3
player_score = 0

list_of_list = [list(elem) for elem in possible_answers]
# print(list_of_list)

for x in list_of_list:
    x[0] = ((x[0].replace(",", "")).replace("/", " ")).lower()
print(list_of_list)

guessed = []
while player_strikes_left > 0:
    player_answer = input("player answer: ")
    # every time set the is_correct to false
    # and check if it is available in answers or not
    # if available then set to true
    is_correct = False
    for i in list_of_list:
        print(i)

        if(player_answer.lower() in i[0]):
            player_score += i[1]
            is_correct = True

    if is_correct == False:
        player_strikes_left -= 1
    print("Player score: " + str(player_score) +
          ", player strikes left: " + str(player_strikes_left))

