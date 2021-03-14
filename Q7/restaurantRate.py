def foodInput():
  foodName = input("Enter in a fast-food restaurant: ")
  return foodName
def rateInput():
  Incorrect = "ERROR"
  foodrate = int(input("What is the rating?: "))
  return foodrate
  while (Incorrect == "error"):
    try:
      foodrate = int(foodrate)
      return foodrate
    except ValueError:
      Incorrect = "ERROR"
      foodrate = input("Invalid restaurant rate, Enter rate: ")
      return foodrate
    else:
      if (foodrate<=0):
        Incorrect = "ERROR"
        foodrate = input("Invalid restaurant rate, Enter rate: ")
        return foodrate
      else:
        return foodrate
    return foodrate

def addData():
  global rate
  global food
  rate=[]
  food=[]
  option = 'y'
  while (option!='n'):
    foodname = foodInput()
    food.append(foodname)
    foodrate = rateInput()
    rate.append(foodrate)
    option = input("Would you like to enter another restaurant?: ")

  return rate
  return food

def analyzeData():
  max = rate[0]
  foodMaxName = food[0]
  min = rate[0]
  foodMinName = food[0]
  print(food)
  for x in range(len(rate)):
    print(rate[x])
    if (max < rate[x]):
      max = rate[x]
      foodMaxName = food[x]
    if (min > rate[x]):
      min = rate[x]
      foodMinName = food[x]
  print("Highest rate is: ",max," and the movie name is ",foodMaxName,sep='')
  print("Lowest rate is: ",min," and the movie name is ",foodMinName,sep='')
  print("Your favourite movie from file is: ", foodMaxName)
