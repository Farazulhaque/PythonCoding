import random
import matplotlib.pyplot as plt


def question1():
    n = int(input("Enter number of tuples: "))
    mytuple = ()
    for i in range(n):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        mytuple = x, y
        print(mytuple)


def question2():
    mylist = []
    mytuple = ()
    for i in range(50):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        mytuple = x, y
        mylist.append((x, y))
    print(mylist)

    x = []
    y = []
    for i in range(len(mylist)):
        x.append(mylist[i][0])
        y.append(mylist[i][1])

    print(x)
    print(y)
    plt.scatter(x, y, color='blue', alpha=0.5, marker='s')
    plt.show()


question1()
question2()
