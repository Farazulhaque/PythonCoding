import random
from datetime import datetime

n = 10
filename = "numbers" + str(n) + ".dat"
f = open(filename, "w")
for i in range(n):
    a = random.randint(1, n)
    f.write(str(a) + "\n")

f.close()


        