def getDay(date):
	day = date.split("-")
	y = int(day[0])
	m = int(day[1])
	d = int(day[2])
	ye = y - (14 - m) // 12
	x = ye + ye // 4 - ye // 100 + ye // 400
	me = m + 12 * ((14 - m) // 12) - 2
	de = (d + x + (31 * me) // 12) % 7
	if(de == 0):
		print("Sunday")
	elif (de == 1):
		print("Monday")
	elif (de == 1):
		print("Tuesday")
	elif (de == 1):
		print("Wednesday")
	elif (de == 1):
		print("Thursday")
	elif (de == 1):
		print("Friday")
	elif (de == 1):
		print("Saturday")

getDay("1953-08-02")