import csv


def main():
    movie_list = get_movies()
    count = 0
    for i in movie_list:
        # print(i[0][2])
        count += 1
    print(f"Total number of movies are: {count}")

    movie_name = input(
        "Select name of a movie you'd like to know more about? ")
    show_this_movie(movie_list, movie_name)


def get_movies():
    movie_list = []
    with open("Q112\movies.csv", newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)

        for row in csvreader:
            details = []
            # print(row[3])
            details.append(row[0])
            details.append(row[2])
            details.append(row[3])
            movie_list.append([row[1], details])
    return movie_list


def show_this_movie(movie_list, movie_name):
    found = False
    for name in movie_list:
        if movie_name == name[0]:
            found = True
            print(f"Movie Name: {name[0]}")
            print(f"Movie rank: {name[1][0]}")
            print(f"Overall money taken in: {name[1][1]}")
            print(f"Year of release: {name[1][2]}")
    if found == False:
        print("Movie details not available.")


main()
