from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pandas as pd
from urlparams.redirect import param_redirect

from . import movie_recommendation, moviedetails, profile, getimages, findbutton

content_type = 'movie'
loggedin = 'false'
idf = 0
searchstr = 'Pirates'
import requests

content_obj = list()


def index(request):
    template = loader.get_template('first.html')
    global searchstr, idf, content_type

    sort = 0
    if request.GET.get('FlipSwitch2') == '1':
        sort = 1

    if request.GET.get('FlipSwitch3') == '1':
        sort = 2
    else:
        sort = 3
    if request.GET.get('FlipSwitch1') == 'tv':
        content_type = 'tv'
    else:
        content_type = 'movie'

    if(request.GET.get('Action')):
        getimages.images("Action", sort, content_type)
        return HttpResponse(template.render())

    if (request.GET.get('Adventure')):
        getimages.images("Adventure", sort, content_type)
        return HttpResponse(template.render())

    if (request.GET.get('Animation')):
        getimages.images("Animation", sort, content_type)
        return HttpResponse(template.render())

    if (request.GET.get('Comedy')):
        getimages.images("Comedy", sort, content_type)
        return HttpResponse(template.render())

    if (request.GET.get('Crime')):
        getimages.images("Crime", sort, content_type)
        return HttpResponse(template.render())

    if (request.GET.get('Documentary')):
        getimages.images("Documentary", sort, content_type)
        return HttpResponse(template.render())

    if (request.GET.get('Drama')):
        getimages.images("Drama", sort, content_type)
        return HttpResponse(template.render())

    if (request.GET.get('Family')):
        getimages.images("Family", sort, content_type)
        return HttpResponse(template.render())

    if (request.GET.get('History')):
        getimages.images("History", sort, content_type)
        return HttpResponse(template.render())

    if (request.GET.get('Horror')):
        getimages.images("Horror", sort, content_type)
        return HttpResponse(template.render())

    if (request.GET.get('Mystery')):
        getimages.images("Mystery", sort, content_type)
        return HttpResponse(template.render())

    if (request.GET.get('Romance')):
        getimages.images("Romance", sort, content_type)
        return HttpResponse(template.render())

    if(request.GET.get('SearchButton')):
        print("Enter")
        searchst = request.GET.get('Editbox1')
        searchstr = searchst
        print("Took input")
        return search(request)

    if (request.GET.get('Button10')):
        idf = findbutton.func("Button10")
        return getdetails(request)
    if (request.GET.get('Button11')):
        idf = findbutton.func("Button11")
        return getdetails(request)

    if (request.GET.get('Button12')):
        idf = findbutton.func("Button12")
        return getdetails(request)

    if (request.GET.get('Button13')):
        idf = findbutton.func("Button13")
        return getdetails(request)

    if (request.GET.get('Button14')):
        idf = findbutton.func("Button14")
        return getdetails(request)

    if (request.GET.get('Button34')):
        idf = findbutton.func("Button34")
        return getdetails(request)

    if (request.GET.get('Button35')):
        idf = findbutton.func("Button35")
        return getdetails(request)

    if (request.GET.get('Button36')):
        idf = findbutton.func("Button36")
        return param_redirect('getdetails')

    if (request.GET.get('Button37')):
        idf = findbutton.func("Button37")
        return param_redirect('getdetails')

    if (request.GET.get('Button38')):
        idf = findbutton.func("Button38")
        return param_redirect('getdetails')

    if (request.GET.get('Button15')):
        idf = findbutton.func("Button15")
        return param_redirect('getdetails')

    if (request.GET.get('Button16')):
        idf = findbutton.func("Button16")
        return param_redirect('getdetails')

    if (request.GET.get('Button17')):
        idf = findbutton.func("Button17")
        return param_redirect('getdetails')

    if (request.GET.get('Button18')):
        idf = findbutton.func("Button18")
        return param_redirect('getdetails')

    if (request.GET.get('Button19')):
        idf = findbutton.func("Button19")
        return param_redirect('getdetails')

    if (request.GET.get('Button39')):
        idf = findbutton.func("Button39")
        return param_redirect('getdetails')

    if (request.GET.get('Button40')):
        idf = findbutton.func("Button40")
        return param_redirect('getdetails')

    if (request.GET.get('Button41')):
        idf = findbutton.func("Button41")
        return param_redirect('getdetails')

    if (request.GET.get('Button42')):
        idf = findbutton.func("Button42")
        return param_redirect('getdetails')

    if (request.GET.get('Button43')):
        idf = findbutton.func("Button43")
        return param_redirect('getdetails')



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
    global idf
    print(idf)
    name, strgenre, strprod, overview, vote, dbid, runtime, release_date, sc = moviedetails.movie(idf, content_type)

    if (request.GET.get('watchlist')):
        data = [dbid, name, strgenre, runtime, release_date, vote, content_type]
        df = pd.DataFrame([data], columns=['imdb', 'name', 'genre', 'duration', 'year', 'rating', 'type'])
        df.to_csv("D:\\mdl\\MDL\\Book1.csv", mode = 'a', header = False, index = False)
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


def search(request):

    global idf
    global searchstr

    search_string = getstring()
    r = requests.get(
        "https://api.themoviedb.org/3/search/movie?api_key=3af4a550e843ce38440160234f2569ed&language=en-US&query=" + search_string + "&page=1&include_adult=false")
    y = r.json()
    res = y['results']
    l = list()
    names = list()
    overviewl = list()
    for i in range(4):
        temp = res[i]
        poster = temp['poster_path']
        overview = temp['overview']
        title = temp['original_title']
        names.append(title)
        overviewl.append(overview)
        id = temp['id']
        l.append(id)
        response = requests.get("https://image.tmdb.org/t/p/w185/" + poster)
        file = open("D:\\mdl\\MDL\\mysite\\polls\\static\\images\\search\\im" + str(i) + ".jpg", "wb")
        file.write(response.content)
        file.close()

    if (request.GET.get('Button1')):
        idf = l[0]
        return getdetails(request)

    if (request.GET.get('Button2')):
        idf = l[1]
        return getdetails(request)

    if (request.GET.get('Button3')):
        idf = l[2]
        return getdetails(request)

    if (request.GET.get('Button4')):
        idf = l[3]
        return getdetails(request)


    return render(request, "search.html", {"n1" : names[0], "n2" : names[1], "n3" : names[2], "n4" : names[3], "o1" : overviewl[0], "o2" : overviewl[1]
                                           , "o3" : overviewl[2], "o4" : overviewl[3]})


def about(request):
    return render(request, "about.html")

def getstring():
    global searchstr
    if(searchstr == ''):
        pass
    else:
        return searchstr