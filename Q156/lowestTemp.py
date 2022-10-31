import csv


def lowestAverageTemperature(filename):
	days = []
	# read csv file and store in days list
	with open(filename, 'r') as file:
		my_reader = csv.reader(file, delimiter=',')
		for row in my_reader:
			days.append(row)
	# set average temperature to mondays average temperature
	averageTemperature = (int(days[0][1]) + int(days[0][2]))/2
	# set monday as lowest temperature day
	lowestTemperatureDay = days[0][0]

	# Loop in days list and calculate average temperature of each days
	# and check with mondays temperature
	# if averageTemperature is greater than any other days average temperature then set average temperature to that day and lowest temperature day to that day 
	for day in days:
		if(averageTemperature > (int(day[1]) + int(day[2]))/2):
			averageTemperature = (int(day[1]) + int(day[2]))/2
			lowestTemperatureDay = day[0]
	print(lowestTemperatureDay)


lowestAverageTemperature("weather.csv")