import random

lives = 3
qstn = 1
correct = 0
while lives > 0 and qstn <= 10:
    operands = ['+', '-', '*', '/']
    i = random.randint(0, len(operands)-1)
    op = operands[i]
    if op in ['+', '-', '*']:
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
    else:
        num1 = random.randint(1, 144)
        num2 = random.randint(1, 144)

    print(f"Question {qstn}")
    print(f"What is {num1} {op} {num2} ?")
    expression = str(num1) + op + str(num2)
    answer = float(eval(expression))
    useranswer = float(input("> "))
    if(answer == useranswer):
        print("CORRECT!")
        correct += 1
    else:
        print("WRONG!")
        lives -= 1
    qstn += 1

if lives != 0:
    print("YOU WIN!")
else:
    print("YOU LOSE!")
print(f"Your score is {correct} out of 10.")
