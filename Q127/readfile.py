import os
filename = "QuestionsAns_Originl.txt"


overlappedquestion = []
overlappedanswer = []
uniquequestion = []
uniqueanswer = []
with open(filename, 'r') as file:
    i = 1
    j = 2
    for line in file:
        if line.startswith("question "):
            if (line[len("question "):] in uniquequestion):
                overlappedquestion.append(line[len("question "):].rstrip("\n"))
                overlappedanswer.append(line[len("answer "):].rstrip("\n"))
            else:
                uniquequestion.append(line[len("question "):].rstrip("\n"))
        if line.startswith("answer "):
            if (line[len("answer "):] in uniqueanswer):
                overlappedquestion.append(line[len("question "):].rstrip("\n"))
                overlappedanswer.append(line[len("answer "):].rstrip("\n"))
            else:
                uniqueanswer.append(line[len("answer "):].rstrip("\n"))

if (len(overlappedanswer) == 0 and len(overlappedquestion) == 0):
    os.rename(filename, "Unique_Pairs.txt")
else:
    with open("Overlapped.txt", "w") as file:
        for i in range(len(overlappedanswer)):
            file.write(overlappedquestion[i])
            file.write(overlappedanswer[i])
            file.write("\n")
