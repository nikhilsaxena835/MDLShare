import requests

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

apiresponse = requests.get(
        "https://api.themoviedb.org/3/trending/"+content_type+"/day?api_key=3af4a550e843ce38440160234f2569ed")

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
            "D:\\mdl\\home\\t" + tempnew + ".jpg",
            "wb")
    file.write(response.content)
    file.close()