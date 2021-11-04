words = []

with open("Q114\words.txt", "r") as file:
    for line in file:
        words.append(line.replace("\n", ""))


sentence = input()
values = sentence.split()

count = 0
for word in values:
    if word in words:
        print(word, end=" ")
    else:
        print(f"**{word}**", end=" ")
        count += 1

print(f"\nCount of incorrecly spelled words: {count}")
