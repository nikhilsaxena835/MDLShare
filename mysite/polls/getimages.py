import requests
import pandas as pd

filteron = False
getfilter = "Action"
language1 = "en-US"
language2 = "hi-IN"
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

dict = {"Action" : 28, "Adventure" : 12, "Animation" : 16, "Comedy" : 35, "Crime" : 80, "Documentary" : 99, "Drama" : 18,
         "Family" : 10751, "Fantasy" : 14, "History" : 36, "Horror" : 27, "Music" : 10402, "Mystery" : 9648, "Romance" : 10749,
         "Science Fiction" : 878, "TV Movie" : 10770, "Thriller" : 53, "War" : 10752, "Western" : 37}

sort = (['popularity.desc', 'popularity.asc', 'vote_average.desc', 'vote_average.asc'])
#if(buttonid == so and so)
sortby = sort[0]

#if radio is on, set type to movie else to tv
content_type = "movie"





key = dict[getfilter]


def savetocsv(result_list):
    df = pd.read_csv("D:\\mdl\\home.csv")
    df3 = pd.DataFrame()
    for i in range(10):
        act.append(result_list[i])
        temp = act[i]
        df3 = df3.append({'tmdb': temp["id"], 'type' : content_type}, ignore_index=True)
        print(df3)

    df3.to_csv("D:\\mdl\\home.csv", mode = 'a', header = False, index = False)


if (filteron):
    apiresponse = requests.get(
        "https://api.themoviedb.org/3/discover/"+content_type+"?api_key=3af4a550e843ce38440160234f2569ed&language="+language2+
        "&sort_by="+sort+"&include_video=true&page=1&with_genres="+key)

    response_to_json = apiresponse.json()

    result_list = response_to_json["results"]

    act = list()

    for i in range(10):
        act.append(result_list[i])
        temp = act[i]
        sc = str(temp["poster_path"])
        response = requests.get("https://image.tmdb.org/t/p/w185/" + sc)
        tempnew = str(i)
        file = open(
            "D:\\mdl\\home\\im" + tempnew + ".jpg",
            "wb")
        file.write(response.content)
        file.close()

    savetocsv(result_list)
else:
    apiresponse = requests.get(
        "https://api.themoviedb.org/3/discover/" + content_type + "?api_key=3af4a550e843ce38440160234f2569ed&language=" + language2 +
        "&sort_by=" + sortby + "&include_video=true&page=1")

    response_to_json = apiresponse.json()

    result_list = response_to_json["results"]

    act = list()

    for i in range(10):
        act.append(result_list[i])
        temp = act[i]
        sc = str(temp["poster_path"])
        response = requests.get("https://image.tmdb.org/t/p/w185/" + sc)
        tempnew = str(i)
        file = open(
            "D:\\mdl\\home\\im" + tempnew + ".jpg",
            "wb")
        file.write(response.content)
        file.close()
    savetocsv(result_list)

apiresponse_trending = requests.get(
        "https://api.themoviedb.org/3/trending/"+content_type+"/day?api_key=3af4a550e843ce38440160234f2569ed")

response_to_json_trending = apiresponse_trending.json()

result_list = response_to_json_trending["results"]

act = list()

for i in range(10):
    act.append(result_list[i])
    temp = act[i]
    sc = str(temp["poster_path"])
    response = requests.get("https://image.tmdb.org/t/p/w185/" + sc)
    tempnew = str(i)
    file = open(
            "D:\\mdl\\home\\t" + tempnew + ".jpg",
            "wb")
    file.write(response.content)
    file.close()
savetocsv(result_list)
'''
Finally a mapping has to be done for individual buttons. The mapping will be on a csv file where we have a column for button id and a column for the movie id.
Another column for content type since API doesnt by itself differentiates between a tv or movie.
If an image button is pressed, then the information is passed to the moviedetails.py and it reads the tmdb id for that movie and then displays the details

'''


