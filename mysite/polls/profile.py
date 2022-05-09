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
    Drama = 1
    Action = 1
    Adventure = 1
    Animation = 1
    Comedy = 1
    Crime = 1
    Documentary = 1
    Horror = 1
    Family = 1
    History = 1
    Mystery = 1
    Romance = 1
    ScienceFiction = 1
    Thriller = 1
    War = 1

    Drama_r = 0
    Action_r = 0
    Adventure_r = 0
    Animation_r = 0
    Comedy_r = 0
    Crime_r = 0
    Documentary_r = 0
    Horror_r = 0
    Family_r = 0
    History_r = 0
    Mystery_r = 0
    Romance_r = 0
    ScienceFiction_r = 0
    Thriller_r = 0
    War_r = 0

    Drama_t = 0
    Action_t = 0
    Adventure_t = 0
    Animation_t = 0
    Comedy_t = 0
    Crime_t = 0
    Documentary_t = 0
    Horror_t = 0
    Family_t = 0
    History_t = 0
    Mystery_t = 0
    Romance_t = 0
    ScienceFiction_t = 0
    Thriller_t = 0
    War_t = 0

    for index, row in df.iterrows():
        print(type(row))
        print(row)

        finder = row['genre']
        if finder.find('Drama') != -1:
            Drama = Drama + 1
            Drama_r = Drama_r + row['rating']
            Drama_t = Drama_t + row['duration']

        if finder.find('Action') != -1:
            Action = Action + 1
            Action_r = Action_r + row['rating']
            Action_t = Action_t + row['duration']

        if finder.find('Adventure') != -1:
            Adventure = Adventure + 1
            Adventure_r = Adventure_r + row['rating']
            Adventure_t = Adventure_t + row['duration']

        if finder.find('Animation') != -1:
            Animation = Animation + 1
            Animation_r = Animation_r + row['rating']
            Animation_t = Animation_t + row['duration']

        if finder.find('Comedy') != -1:
            Comedy = Comedy + 1
            Comedy_r = Comedy_r + row['rating']
            Comedy_t = Comedy_t + row['duration']

        if finder.find('Crime') != -1:
            Crime = Crime + 1
            Crime_r = Crime_r + row['rating']
            Crime_t = Crime_t + row['duration']

        if finder.find('Documentary') != -1:
            Documentary = Documentary + 1
            Documentary_r = Documentary_r + row['rating']
            Documentary_t = Documentary_t + row['duration']

        if finder.find('History') != -1:
            History = History + 1
            History_r = History_r + row['rating']
            History_t = History_t + row['duration']

        if finder.find('Horror') != -1:
            Horror = Horror + 1
            Horror_r = Horror_r + row['rating']
            Horror_t = Horror_t + row['duration']

        if finder.find('Family') != -1:
            Family = Family + 1
            Family_r = Family_r + row['rating']
            Family_t = Family_t + row['duration']


        if finder.find('Mystery') != -1:
            Mystery = Mystery + 1
            Mystery_r = Mystery_r + row['rating']
            Mystery_t = Mystery_t + row['duration']


        if finder.find('Romance') != -1:
            Romance = Romance + 1
            Romance_r = Romance_r + row['rating']
            Romance_t = Romance_t + row['duration']

        if finder.find('Science Fiction') != -1:
            ScienceFiction = ScienceFiction + 1
            ScienceFiction_r = ScienceFiction_r + row['rating']
            ScienceFiction_t = ScienceFiction_t + row['duration']


        if finder.find('Thriller') != -1:
            Thriller = Thriller + 1
            Thriller_r = Thriller_r + row['rating']
            Thriller_t = Thriller_t + row['duration']

        if finder.find('War') != -1:
            War = War + 1
            War_r = War_r + row['rating']
            War_t = War_t + row['duration']


    x = np.array(['Drama', 'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'History', 'Horror', 'Family', 'Mystery',
                  'Romance', 'Science Fiction', 'Thriller', 'War'])
    y = np.array([Drama, Action, Adventure, Animation, Comedy, Crime, Documentary, History, Horror, Family,  Mystery,
                  Romance, ScienceFiction, Thriller, War])



    Drama_r = Drama_r / Drama
    Action_r = Action_r/Action
    Adventure_r = Adventure_r/Adventure
    Animation_r = Animation_r / Animation
    Comedy_r = Comedy_r / Comedy
    Crime_r = Crime_r / Crime
    Documentary_r = Documentary_r/Documentary
    Horror_r = Horror_r/Horror
    Family_r = Family_r/Family
    History_r = History_r/History
    Mystery_r = Mystery_r/Mystery
    Romance_r = Romance_r/Romance
    ScienceFiction_r = ScienceFiction_r/ScienceFiction
    Thriller_r = Thriller_r/Thriller
    War_r = War_r/War

    y_for_ratings = np.array([Drama_r, Action_r, Adventure_r, Animation_r, Comedy_r, Crime_r, Documentary_r, History_r, Horror_r, Family_r, Mystery_r,
                  Romance_r, ScienceFiction_r, Thriller_r, War_r])

    y_for_time = np.array([Drama_t, Action_t, Adventure_t, Animation_t, Comedy_t, Crime_t, Documentary_t, History_t, Horror_t, Family_t, Mystery_t,
                  Romance_t, ScienceFiction_t, Thriller_t, War_t])


    plt.bar(x, y_for_ratings, 0.6)
    plt.xticks(rotation=90)
    plt.savefig("D:\\mdl\\MDL\\mysite\\polls\\static\\images\\plots\\ratings.jpg")

    plt.bar(x, y_for_time, 0.6)
    plt.xticks(rotation=90)
    plt.savefig("D:\\mdl\\MDL\\mysite\\polls\\static\\images\\plots\\duration.jpg")


    plt.bar(x, y, 0.6)
    plt.xticks(rotation = 90)
    plt.savefig("D:\\mdl\\MDL\\mysite\\polls\\static\\images\\plots\\genre.jpg")

