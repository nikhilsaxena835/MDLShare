import requests
import pandas as pd


def tata():
    df = pd.read_csv("E:\\Book1.csv")
    z = 0
    a = list()
    b = list()
    c = list()
    for index, row in df.iterrows():
        b = [row['id'], row['name'], row['genre']]
        a.append(b)
    print(a)

    for r in a:
        print(r[0])
        for x in r:
            print(x)
    lenth = len(a)
    print(lenth)





tata()

