import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def starbacks():

    starbacks = pd.read_csv("directory.csv")

    #print(starbacks.head())

    count = starbacks.groupby(["Country"]).count()

    count["Brand"].plot(kind='bar',figsize = (20,8))

    count_state = starbacks.groupby(["Country", "State/Province"]).count()

    plt.xlabel("Country")
    plt.ylabel("Number of store")
    plt.title("Number of Starbacks store in each country", fontsize=20)

    print(count_state)

    plt.savefig("./starbacks_store.png")

    plt.show()

    return None

starbacks()