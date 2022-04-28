from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pandas as pd



import requests

def index(request):
  template = loader.get_template('first.html')
  return HttpResponse(template.render())

def add(request):
    n = nana()
    return render(request, "searchhtml.html", {"Name" : n[0], "UserScore" : n[1]})

def lists(request):
    rows,c, lenth = tata()
    x = int(0)
    y = int(0)
    return render(request, "layerlists.html", {"rows" : rows, "c" : c, "lenth" : lenth})

def reclists(request):
    rows,c, lenth = tata1()
    x = int(0)
    y = int(0)
    return render(request, "rec_lists.html", {"rows" : rows, "c" : c, "lenth" : lenth})


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
        file = open("D:\\mdl\\details\\cr" + tempnew + ".jpg", "wb")
        file.write(response.content)
        file.close()

    name = l["original_title"]
    scn = str(l["poster_path"])
    response1 = requests.get("https://image.tmdb.org/t/p/w185/" + scn)
    file = open("D:\\mdl\\details\\crb.jpg", "wb")
    file.write(response1.content)
    file.close()

    pop = l["popularity"]
    st = ([name, pop])
    print(name, pop, scn)
    return st

def tata():

    df = pd.read_csv("E:\\Book1.csv")
    z = 0
    a = list()
    b = list()
    c = list()
    for index, row in df.iterrows():
        b = [row['imdb'], row['name'], row['genre'], row['stream'], row['duration'], row['year'], row['rating']]
        a.append(b)
    lenth = len(a)

    return a,c, lenth

def tata1():
    df = pd.read_csv("E:\\Book2.csv")
    z = 0
    a = list()
    b = list()
    c = list()
    for index, row in df.iterrows():
        b = [row['id'], row['name'], row['rating'], row['year'], row['overview'], row['genre'], row['type']]
        a.append(b)
    lenth = len(a)

    return a,c, lenth
