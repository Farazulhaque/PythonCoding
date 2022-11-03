country_perCapita = {}
with open('rawdata2004.txt', 'r') as file:
	for line in file:
		data = line.split("$")
		country_perCapita[data[0].rstrip()] = "".join(data[1].rsplit())

country_name = input("Enter country name (or type quit): ")
if(country_name != "quit"):
	print(f"The per capita income is $ {country_perCapita[country_name]}")
# print(country_perCapita['Qatar'])