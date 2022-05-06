import requests

def movie():
    r = requests.get("https://api.themoviedb.org/3/movie/4953?api_key=3af4a550e843ce38440160234f2569ed&language=en-US")
    nr = requests.get(
        "https://api.themoviedb.org/3/movie/4953/credits?api_key=3af4a550e843ce38440160234f2569ed&language=en-US")

    l = r.json()
    z = nr.json()
    dbid = 4953
    name = l['original_title']
    genre = l['genres']
    strgenre = ""
    strprod = ""
    runtime = l['runtime']
    release_date = l['release_date']

    for i in genre:
        temp = i
        key = temp['name']
        strgenre = strgenre+str(key)+ "  "

    overview = l['overview']
    production = l['production_companies']

    for i in production:
         temp = i
         key = temp['name']
         strprod = strprod+str(key)+", \n"

    vote = l['vote_average']
    crew = z["cast"]
    sp = list()


    for i in range(4):
      temp = crew[i]
      sc = str(temp["profile_path"])
      sp.append(temp["name"])
      response = requests.get("https://image.tmdb.org/t/p/w185/" + sc)
      tempnew = str(i)
      file = open("D:\\mdl\\details\\cr" + tempnew + ".jpg", "wb")
      file.write(response.content)
      file.close()


    scn = str(l["poster_path"])
    response1 = requests.get("https://image.tmdb.org/t/p/w185/" + scn)
    file = open("D:\\mdl\\details\\crb.jpg","wb")
    file.write(response1.content)
    file.close()

    return name, strgenre, strprod, overview, vote, dbid, runtime, release_date, l['poster_path']


movie()