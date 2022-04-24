
import requests

r = requests.get("https://api.themoviedb.org/3/trending/all/day?api_key=3af4a550e843ce38440160234f2569ed")

y = r.json()

l = y["results"]

act = list()

for i in range(10):

    act.append(l[i])
    temp = act[i]
    sc = str(temp["poster_path"])
    response = requests.get("https://image.tmdb.org/t/p/w185/"+sc)
    tempnew = str(i)
    file = open("C:\\Users\\nikhil\\PycharmProjects\\pythonProject6\\mysite\\polls\\templates\\images\\t"+tempnew+".jpg", "wb")
    file.write(response.content)
    file.close()

