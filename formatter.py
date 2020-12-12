f = open('result.txt', 'r')
f_places = open('places.csv', 'w')
f_ratings = open('ratings.csv', 'w')

while True:
    line1 = f.readline().strip()
    line2 = f.readline().strip()
    line3 = f.readline().strip()

    if not line1 or not line2 or not line3:
        break

    place_info = line1.replace('/', ',')
    name = line1.split('/')[0]
    # print(place_info)

    usernames = line2.replace('\'\'', '').strip('[]').split(', ')
    usernames = [x.strip("''") for x in usernames]
    # print(usernames)

    ratings = line3.replace('\'\'', '').strip('[]').split(', ')
    ratings = [x.strip("''") for x in ratings]
    # print(ratings)

    print()

    # csv - places
    print(place_info + '\n', end='')
    f_places.write(place_info + '\n')

    # csv - ratings
    for i in range(len(usernames)):
        print(usernames[i] + ',' + name + ',' + ratings[i] + '\n', end='')
        f_ratings.write(usernames[i] + ',' + name + ',' + ratings[i] + '\n')

f_ratings.close()
f_places.close()
f.close()
