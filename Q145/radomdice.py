import random


def RollDice():
    score = 0
    dice_roll = []
    for i in range(5):
        rolls = random.randint(1, 6)
        score += rolls
        dice_roll.append(rolls)
    return score, dice_roll


def PlayGame():
    for i in range(6):
        dice_roll = []
        score = 0
        score, dice_roll = RollDice()
        if score < 10:
            score += 20
            print(f"\n{score}:", end="")
            for i in dice_roll:
                print(i, end=" ")
            print(" - bonus 20 points!", end="")
        else:
            print(f"\n{score}:", end="")
            for i in dice_roll:
                print(i, end=" ")


PlayGame()
