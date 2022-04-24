import pandas as pd
import os.path


check = os.path.exists("D:\\user.csv")


def func(st, passw):
    if(check):
        df = pd.read_csv("D:\\user.csv")
        getp = df.loc[df["user"]==st]
        if(getp == passw):
            print("You are logged in")
        else:
            print("Wrong pass retry")
    else:
        print("You need to create acc first")
        df = pd.DataFrame(columns=['id', 'name', 'runtime'])
        df.to_csv("D:\\user.csv", columns=['id', 'name', 'runtime'])


func('sdf', 'sdf')
