import requests
import pandas as pd
import json
r = requests.get("https://api.themoviedb.org/3/movie/300?api_key=3af4a550e843ce38440160234f2569ed")
r
print(r.text)

y = r.json()
l = y["genres"]
print(type(l))

a = l[0]
b = l[1]
c = l[2]
print(type(a))

one = a["name"]
two = b["name"]
three = c["name"]
n = y["original_title"]
runtime = y["runtime"]
d = y["release_date"]
print(y["genres"])

data = {
    'name': [n],
    'genre': [one],
    'duration': [runtime],
    'year': [d]
}

df = pd.DataFrame(data)

# append data frame to CSV file
df.to_csv('E:\\Book1.csv', mode='a', index=False, header=False)

response = requests.get("https://image.tmdb.org/t/p/original/bOGkgRGdhrBYJSLpXaxhXVstddV.jpg")

file = open("C:\\Users\\nikhil\\PycharmProjects\\pythonProject6\\mysite\\polls\\static\\dj_app\\media\\im2.jpg", "wb")
file.write(response.content)
file.close()
