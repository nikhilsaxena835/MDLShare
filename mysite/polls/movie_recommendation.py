import os

import requests
import pandas as pd

import requests
import math

my_dict = {28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy", 80: "Crime", 99: "Documentary", 18: "Drama",
           10751: "Family", 14: "Fantasy",
           36: "History", 27: "Horror", 10402: "Music", 9648: "Mystery", 10749: "Romance", 878: "Science Fiction",
           10770: "TV Movie", 53: "Thriller",
           10752: "War", 37: "Western"}

df = pd.read_csv("E:\\Book1.csv")
temp = list()
biglist = list()
checker = list()
lala = list()
count = 0
for i in df.iterrows():
    checker.append(df['type'].values[count])
    count = count + 1

count = 0
checknew = 0
readc = pd.read_csv("E:\\Book2.csv")
for i in df.iterrows():
    print(i, checknew)
    '''
    if checknew == 0:
        checknew = 1
        continue
        '''
    key = list()
    if (checker[count] == "movie"):
        content = 'movie'
    else:
        content = 'tv'
    tmdb = str(df['imdb'].values[count])
    r = requests.get(
        "https://api.themoviedb.org/3/" + content + "/" + tmdb + "/recommendations?api_key=3af4a550e843ce38440160234f2569ed&language=en-US&page=1")
    y = r.json()
    print(y)
    print(type(y))
    count = count + 1
    if y:
        l1 = y["results"]
        if l1:
            print(type(l1))
            lala = l1[0]
            newid = lala['id']
            newposter = lala['poster_path']
            newname = lala['original_title']
            newrating = lala['vote_average']
            newyear = lala['release_date']
            overview = lala['overview']
            genre = lala['genre_ids']
            content_type = lala['media_type']

            for i in genre:
                print(i)

                temp1 = my_dict[i]
                print(temp1)
                key.append(temp1)

            temp = [newid, newname, newrating, key, overview, newyear, content_type]
            data = {'id' : newid, 'name' : newname, 'rating' : newrating, 'year' : newyear, 'overview' : overview, 'genre' : key, 'type' : content_type}
            df1 = pd.DataFrame(data)
            df1.to_csv("E:\\Book2.csv", mode = 'w', index=False, header=False)
            biglist.append(temp)
print(biglist)
'''
act = list()

for i in biglist:

    temp = i
    newid = temp['id']
    newposter = temp['poster_path']
    newname = temp['original_title']
    newrating = temp['vote_average']
    newyear = temp['release_date']
    overview = temp['overview']
    genre = temp['genre_ids']
    content_type = temp['media_type']

    act.append(l[i])
    temp = act[i]
    sc = str(temp["poster_path"])
    response = requests.get("https://image.tmdb.org/t/p/w185/"+sc)
    tempnew = str(i)
    file = open("C:\\Users\\nikhil\\PycharmProjects\\pythonProject6\\mysite\\polls\\templates\\images\\t"+tempnew+".jpg", "wb")
    file.write(response.content)
    file.close()
'''

