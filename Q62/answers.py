def main():
    filename = "answers.txt"
    # To store answers stored in answers.txt in answers list
    answers = []
    # Open file to read
    with open(filename, "r") as file:
        # Loop over each line
        for name in file:
            # Added each answer into list by removing newline character("\n") from each line
            answers.append(name.rstrip("\n"))
            
    correct_answers = ['A', 'B', 'C', 'D', 'D', 'C', 'B', 'A', 'A', 'C']
    count_correct = 0
    for i in range(10):
        if correct_answers[i] == answers[i]:
            count_correct += 1
    print(f"No of Correct Answers: {count_correct}")
    print(f"No of Incorrect Answers: {10 - count_correct}")
    if count_correct != 10:
        print(f"Correct Answers are : {correct_answers}")
        print(f"Your Answers are    : {answers}")
    if count_correct >= 8:
        print("Good Job!!")


main()
