my_tuple = ("NoTimeToDie DanielCraige UK", "MissionImpossible TomCruise USA",
            "TopGun TomCruise USA", "Troy BradPitt USA",
            "Skyfall DanielCraige UK", "TheTheoryOfEveryting EddieRedmayne UK",
            "FantasticBeast EddieRedmayne UK", "Seven BradPitt USA")

ids = []
for i in range(len(my_tuple)):
    data = my_tuple[i].split()
    actor = data[1]
    country = data[2]
    id = ""
    if country == "UK":
        id += "1"
    elif country == "USA":
        id += "2"

    if actor == "DanielCraige":
        id += "01"
    elif actor == "TomCruise":
        id += "02"
    elif actor == "BradPitt":
        id += "03"
    elif actor == "EddieRedmayne":
        id += "04"
    id += str(i)
    ids.append(id)

dict = {}
usa_value = []
uk_value = []
for i in range(len(my_tuple)):
    data = my_tuple[i].split()
    movie_name = data[0]
    usa_tup = []
    uk_tup = []
    if "USA" in data:
        usa_tup.append(movie_name)
        usa_tup.append(ids[i])
        usa_tup = tuple(usa_tup)
        usa_value.append(usa_tup)
    if "UK" in data:
        uk_tup.append(movie_name)
        uk_tup.append(ids[i])
        uk_tup = tuple(uk_tup)
        uk_value.append(uk_tup)
dict["USA"] = usa_value
dict["UK"] = uk_value
print(dict)
