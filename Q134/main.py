import os

os.mkdir("cs104")
with open("cs104/notes.txt", "w") as file:
    file.write("I like computer programming")

os.mkdir("cs104/slides")
with open("cs104/slides/lecture01.txt", "w") as file:
    file.write("lecture 01:\n\"Introduction\"")

os.mkdir("cs104/labs")
os.mkdir("cs104/labs/lab01")
os.mkdir("cs104/labs/lab02")
os.mkdir("cs104/labs/lab02/solutions")

with open("cs104/labs/lab02/solution.py", "w") as file:
    file.write("print(\"hello\"")
    file.write("for i in range(5):")
    file.write("\tprint(i**2)")
