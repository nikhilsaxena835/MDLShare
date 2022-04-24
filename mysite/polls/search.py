
import requests

def nana():
    st = "The"
    r = requests.get("https://api.themoviedb.org/3/search/company?api_key=3af4a550e843ce38440160234f2569ed&query="+st+"&page=1")

    y = r.json()

    l = y["results"]

    act = list()
    print(type(act))
    a = act[0]
    s = a["name"]
    return s
