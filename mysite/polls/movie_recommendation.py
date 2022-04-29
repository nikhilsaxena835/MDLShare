import pandas as pd
import requests

def save_images():
    my_dict = {28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy", 80: "Crime", 99: "Documentary", 18: "Drama",
               10751: "Family", 14: "Fantasy",
               36: "History", 27: "Horror", 10402: "Music", 9648: "Mystery", 10749: "Romance", 878: "Science Fiction",
               10770: "TV Movie", 53: "Thriller",
               10752: "War", 37: "Western"}
    headerlist = ['id', 'name', 'rating', 'year', 'overview', 'genre', 'type']
    posterlist = list()
    dforiginal = pd.DataFrame()
    ids = list()
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
    for i in df.iterrows():

        if checknew == 0:
            checknew = 1
            continue

        key = list()
        if (checker[count] == "movie"):
            content = 'movie'
        else:
            content = 'tv'
        tmdb = str(df['imdb'].values[count])
        r = requests.get(
            "https://api.themoviedb.org/3/" + content + "/" + tmdb + "/recommendations?api_key=3af4a550e843ce38440160234f2569ed&language=en-US&page=1")
        y = r.json()
        count = count + 1
        if y:
            l1 = y["results"]
            if l1:
                lala = l1[0]
                newid = lala['id']
                newposter = lala['poster_path']
                newname = lala['original_title']
                newrating = lala['vote_average']
                newyear = lala['release_date']
                overview = lala['overview']
                genre = lala['genre_ids']
                content_type = lala['media_type']
                posterlist.append(newposter)
                ids.append(newid)
                for i in genre:
                    temp1 = my_dict[i]
                    key.append(temp1)

                temp = [newid, newname, newrating, key, overview, newyear, content_type]
                data = {'id' : newid, 'name' : newname, 'rating' : newrating, 'year' : newyear, 'overview' : overview, 'genre' : [key], 'type' : content_type}
                df1 = pd.DataFrame(data)

                dforiginal = dforiginal.append(df1)
                biglist.append(temp)
                tempnew = str(newid)
                response = requests.get("https://image.tmdb.org/t/p/w185/" + newposter)
                file = open("D:\\mdl\\home\\rec" + tempnew + ".jpg", "wb")
                file.write(response.content)
                file.close()

    dforiginal.to_csv("E:\\Book2.csv", mode='w', index=False, header=headerlist)



