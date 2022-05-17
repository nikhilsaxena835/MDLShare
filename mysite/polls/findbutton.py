import pandas as pd

def func(button):
    r = 0

    df = pd.read_csv("D:\\mdl\\MDL\\home.csv", header=None)

    if button == "Button10":
        id = df.iloc[[0],[0]]

        r = int(id.iat[0,0])

    if button == "Button11":
        id = df.iloc[[1],[0]]

        r = int(id.iat[0,0])

    if button == "Button12":
        id = df.iloc[[2],[0]]

        r = int(id.iat[0,0])

    if button == "Button13":
        id = df.iloc[[3],[0]]

        r = int(id.iat[0,0])

    if button == "Button14":
        id = df.iloc[[4],[0]]

        r = int(id.iat[0,0])

    if button == "Button34":
        id = df.iloc[[5],[0]]

        r = int(id.iat[0,0])

    if button == "Button35":
        id = df.iloc[[6],[0]]

        r = int(id.iat[0,0])

    if button == "Button36":
        id = df.iloc[[7],[0]]

        r = int(id.iat[0,0])

    if button == "Button37":
        id = df.iloc[[8],[0]]

        r = int(id.iat[0,0])

    if button == "Button38":
        id = df.iloc[[9],[0]]

        r = int(id.iat[0,0])

    if button == "Button15":
        id = df.iloc[[10],[0]]

        r = int(id.iat[0,0])

    if button == "Button16":
        id = df.iloc[[11],[0]]

        r = int(id.iat[0,0])

    if button == "Button17":
        id = df.iloc[[12],[0]]

        r = int(id.iat[0,0])

    if button == "Button18":
        id = df.iloc[[13],[0]]

        r = int(id.iat[0,0])

    if button == "Button19":
        id = df.iloc[[14],[0]]

        r = int(id.iat[0,0])

    if button == "Button40":
        id = df.iloc[[15],[0]]

        r = int(id.iat[0,0])

    if button == "Button39":
        id = df.iloc[[16],[0]]

        r = int(id.iat[0,0])

    if button == "Button41":
        id = df.iloc[[17],[0]]

        r = int(id.iat[0,0])

    if button == "Button42":
        id = df.iloc[[18],[0]]

        r = int(id.iat[0,0])

    if button == "Button43":

        id = df.iloc[[19], [0]]
        r = int(id.iat[0, 0])

    return r

