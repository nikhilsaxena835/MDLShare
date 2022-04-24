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
        file = open("D:\\mdl\\details\\cr" + tempnew + ".jpg","wb")
        file.write(response.content)
        file.close()

    name = l["original_title"]
    scn = str(l["poster_path"])
    response1 = requests.get("https://image.tmdb.org/t/p/w185/" + scn)
    file = open("D:\\mdl\\details\\crb.jpg","wb")
    file.write(response1.content)
    file.close()

    pop = l["popularity"]
    st = ([name, pop])
    print(name, pop, scn)
    return st

