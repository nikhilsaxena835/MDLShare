import requests


s = "action"
r = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=3af4a550e843ce38440160234f2569ed&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres="+s)

y = r.json()

l = y["results"]

act = list()

for i in range(10):

    act.append(l[i])
    temp = act[i]
    sc = str(temp["poster_path"])
    response = requests.get("https://image.tmdb.org/t/p/w185/"+sc)
    tempnew = str(i)
    file = open("C:\\Users\\nikhil\\PycharmProjects\\pythonProject6\\mysite\\polls\\templates\\images\\im"+tempnew+".jpg", "wb")
    file.write(response.content)
    file.close()

