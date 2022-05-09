from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pandas as pd


from . import movie_recommendation, moviedetails, profile

content = 'movie'
loggedin = 'false'
import requests

content_obj = list()


def index(request):
    if(request.GET.get('Action')):
        print("Button 10 pressed")
    template = loader.get_template('first.html')
    return HttpResponse(template.render())


def add(request):
    n = nana()
    return render(request, "searchhtml.html", {"Name" : n[0], "UserScore" : n[1]})


def lists(request):
    rows = fetch_watchlist()
    return render(request, "lists.html", {"rows": rows})


def reclists(request):
    rows = fetch_recommendation()
    return render(request, "rec_lists.html", {"rows": rows})


def getdetails(request):
    name, strgenre, strprod, overview, vote, dbid, runtime, release_date, sc = moviedetails.movie()
    if (request.GET.get('watchlist')):
        data = [dbid, name, strgenre, runtime, release_date, vote, content]
        df = pd.DataFrame([data], columns=['imdb', 'name', 'genre', 'duration', 'year', 'rating', 'type'])
        df.to_csv("E:\\Book1.csv", mode = 'a', header = False, index = False)
        response = requests.get("https://image.tmdb.org/t/p/w185/" + sc)
        tempnew = str(dbid)
        file = open(
            "D:\\mdl\\MDL\\mysite\\polls\\static\\images\\watchlist\\im" + tempnew + ".jpg",
            "wb")
        file.write(response.content)
        file.close()

    return render(request, "movie_details.html", {"Name" : name, "Genre" : strgenre, "Production" : strprod, "Overview" : overview, "Vote" : vote})

# originally was intended for search bar, this function is obsolete for now


def nana():
    import requests

    r = requests.get("https://api.themoviedb.org/3/movie/550?api_key=3af4a550e843ce38440160234f2569ed&language=en-US")
    nr = requests.get(
        "https://api.themoviedb.org/3/movie/550/credits?api_key=3af4a550e843ce38440160234f2569ed&language=en-US")

    y = r.json()
    z = nr.json()
    print(type(y))
    l = y
    m = z["cast"]
    sp = list()

    for i in range(4):
        temp = m[i]
        sc = str(temp["profile_path"])
        sp.append(temp["name"])
        response = requests.get("https://image.tmdb.org/t/p/w185/" + sc)
        tempnew = str(i)
        file = open("D:\\mdl\\MDL\\mysite\\polls\\static\\images\\details\\cr" + tempnew + ".jpg", "wb")
        file.write(response.content)
        file.close()

    name = l["original_title"]
    scn = str(l["poster_path"])
    response1 = requests.get("https://image.tmdb.org/t/p/w185/" + scn)
    file = open("D:\\mdl\\MDL\\mysite\\polls\\static\\images\\details\\crb.jpg", "wb")
    file.write(response1.content)
    file.close()

    pop = l["popularity"]
    st = ([name, pop])
    print(name, pop, scn)
    return st


def fetch_watchlist():

    df = pd.read_csv("D:\\mdl\\MDL\\Book1.csv")
    rows_as_list = list()
    for index, row in df.iterrows():
        temp = [row['imdb'], row['name'], row['genre'], row['duration'], row['year'], row['rating']]
        rows_as_list.append(temp)

    return rows_as_list


def fetch_recommendation():
    movie_recommendation.save_images()
    df = pd.read_csv("D:\\mdl\\MDL\\Book2.csv")
    rows_as_list = list()
    for index, row in df.iterrows():
        temp = [row['id'], row['name'], row['rating'], row['year'], row['overview'], row['genre'], row['type']]
        rows_as_list.append(temp)

    return rows_as_list


def login(request):
    global loggedin
    userid = request.GET.get('username')
    passwrd = request.GET.get('password')
    df = pd.read_csv("D:\\mdl\\MDL\\mysite\\users.csv")
    df = df.loc[df['userid'] == userid]

    print(df)
    userpass = df['password'].values
    if userpass == passwrd:
        loggedin = 'true'
        print('You are now logged in')
        print(loggedin)
    return render(request, "login.html")


def profile_page(request):
    profile.generate_charts()
    return render(request, "profile.html")
