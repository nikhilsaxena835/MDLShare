import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Dictionary from TMDB
my_dict = [{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 16, "name": "Animation"},
{"id": 35, "name": "Comedy"}, {"id": 80, "name": "Crime"}, {"id": 99, "name": "Documentary"},
{"id": 18, "name": "Drama"}, {"id": 10751, "name": "Family"}, {"id": 14, "name": "Fantasy"},
{"id": 36, "name": "History"}, {"id": 27, "name": "Horror"}, {"id": 10402, "name": "Music"},
{"id": 9648, "name": "Mystery"}, {"id": 10749, "name": "Romance"},
{"id": 878, "name": "Science Fiction"}, {"id": 10770, "name": "TV Movie"},
{"id": 53, "name": "Thriller"}, {"id": 10752, "name": "War"},
{"id": 37, "name": "Western"}]
'''


def generate_charts():
    df = pd.read_csv("D:\\mdl\\MDL\\Book1.csv")
    print(type(df['genre']))
    Drama = 0
    Action = 0
    Adventure = 0
    Animation = 0
    Comedy = 0
    Crime = 0
    Documentary = 0
    Horror = 0
    Family = 0
    Fantasy = 0
    History = 0
    Music = 0
    Mystery = 0
    Romance = 0
    ScienceFiction = 0
    TVMovie = 0
    Thriller = 0
    War = 0
    Western = 0
    dramar = 0

    for index, row in df.iterrows():
        print(type(row))
        print(row)


# Pari boy upar wali line aur niche wala pehla if dekho ... aise karne ka hai sabki rating find ... end mein divide bhi karna hai toh wo uske counter
# variable means jese ki Drama hai toh uska total aara hai 53.59999 toh usko Drama variable se divide krne ka .. isse uski rating aa jaegi. Simple it was kya yrrr
# ab aisa hi sabka kardo .. mein jara hu dusri taraf firse hue hue hue
        finder = row['genre']
        if finder.find('Drama') != -1:
            Drama = Drama + 1
            #ye niche wali line
            dramar = dramar + row['rating']

        if finder.find('Action') != -1:
            Action = Action + 1

        if finder.find('Adventure') != -1:
            Adventure = Adventure + 1

        if finder.find('Animation') != -1:
            Animation = Animation + 1

        if finder.find('Comedy') != -1:
            Comedy = Comedy + 1

        if finder.find('Crime') != -1:
            Crime = Crime + 1

        if finder.find('Documentary') != -1:
            Documentary = Documentary + 1

        if finder.find('History') != -1:
            History = History + 1

        if finder.find('Horror') != -1:
            Horror = Horror + 1

        if finder.find('Family') != -1:
            Family = Family + 1

        if finder.find('Fantasy') != -1:
            Fantasy = Fantasy + 1

        if finder.find('Mystery') != -1:
            Mystery = Mystery + 1

        if finder.find('Music') != -1:
            Music = Music + 1

        if finder.find('Romance') != -1:
            Romance = Romance + 1

        if finder.find('Science Fiction') != -1:
            ScienceFiction = ScienceFiction + 1

        if finder.find('TV Movie') != -1:
            TVMovie = TVMovie + 1

        if finder.find('Thriller') != -1:
            Thriller = Thriller + 1

        if finder.find('War') != -1:
            War = War + 1

        if finder.find('Western') != -1:
            Western = Western + 1

    x = np.array(['Drama', 'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'History', 'Horror', 'Family', 'Fantasy', 'Mystery', 'Music',
                  'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western'])
    y = np.array([Drama, Action, Adventure, Animation, Comedy, Crime, Documentary, History, Horror, Family, Fantasy, Mystery,
                  Music, Romance, ScienceFiction, TVMovie, Thriller, War, Western])

    print(dramar)
    plt.bar(x, y)
    plt.show()


generate_charts()
