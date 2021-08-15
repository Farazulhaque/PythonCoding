file1 = "firstFile.txt"
file2 = "secondFile.txt"
file1_words = []
file2_words = []

try:
    with open(file1) as input_data:
        for each_line in input_data:
            word = each_line.strip()
            file1_words.append(word)
except:
    print(f'Error accessing {file1}')

try:
    with open(file2) as input_data:
        for each_line in input_data:
            word = each_line.strip()
            file2_words.append(word)
except:
    print(f'Error accessing {file2}')

file1_words = set(file1_words)
file1_words = list(file1_words)
file2_words = set(file2_words)
file2_words = list(file2_words)


print("\nList of all the unique words contained in both files: ")
unique = []
for words in file1_words:
    unique.append(words)
for words in file2_words:
    unique.append(words)
print(unique)

print("\nList of the words that appear in both files: ")
both = []
for word in file1_words:
    if word in file2_words:
        both.append(word)
print(both)

print("\nList of the words that appear in the first file but not in the second file")
firstNotSecond = []
for word in file1_words:
    if word not in file2_words:
        firstNotSecond.append(word)
print(firstNotSecond)

print("\nList of the words that appear in the second file but not in the first file")
secondNotFirst = []
for word in file2_words:
    if word not in file1_words:
        secondNotFirst.append(word)
print(secondNotFirst)

print("\nList of the words that appear in either the first or second file but not both")
notBoth = []
for word1 in file1_words:
    if word1 not in file2_words:
        notBoth.append(word1)

for word2 in file2_words:
    if word2 not in file1_words:
        notBoth.append(word2)
print(notBoth)
