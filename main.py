import pandas as pd;
import matplotlib.pyplot as plt
df = pd.read_csv("E:\\Book1.csv")
print(df.head())
df["year"].plot(kind="hist")
plt.title("Era you like")
plt.ylabel("Number")
plt.xlabel("Year")
plt.show()

l = df["genre"].tolist()
print(l)
count = 0
i = 0
for i in range(len(l)):
    word = str(l[i])
    for s in word:
        print(word)
        if (s=="Drama"):
            count= count+1
    print(l[i])

print(count)
print(type(l))
print(type(l[0]))