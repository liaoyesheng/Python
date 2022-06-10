import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

movie = pd.read_csv("IMDB-Movie-Data.csv")

#print(movie.head())


#count_director = np.unique(movie["Director"]).shape[0]

#print(count_director)

def Rate():
    #creat figure and show it
    #movie["Rating"].plot(kind="hist")

    plt.figure(figsize=(20,8),dpi=100)

    plt.hist(movie["Rating"].values, bins=20)

    #add scale

    max_ = movie["Rating"].max()
    min_ = movie["Rating"].min()

    t1 = np.linspace(min_, max_ , num=21)

    plt.xticks(t1)

    #add image grid
    plt.grid()

    plt.xlabel("score of movie")
    plt.ylabel("Number of movie")
    plt.title("score of movie", fontsize=20)


    #show it!
    plt.show()

    return None


def runtime():
    #Runtime(Minutes)

    plt.figure(figsize=(20,8),dpi=100)

    plt.hist(movie["Runtime (Minutes)"].values, bins=20)

    #add scale

    max_ = movie["Runtime (Minutes)"].max()
    min_ = movie["Runtime (Minutes)"].min()

    t1 = np.linspace(min_, max_ , num=21)

    plt.xticks(t1)

    #add image grid
    plt.grid()

    plt.xlabel("runtime of movie")
    plt.ylabel("Number of movie")
    plt.title("runtime of movie", fontsize=20)

    #show it!
    plt.show()

    return None

def Classify():

    #movie["Genre"]
    temp_list = [i.split(",") for i in movie["Genre"]]
    genre_list = np.unique([i for j in temp_list for i in j])
    zeros = np.zeros([movie.shape[0], genre_list.shape[0]])

    temp_movie = pd.DataFrame(zeros, columns=genre_list)


    #for loop
    for i in range(1000):
        temp_movie.loc[i,temp_list[i]] = 1 #we search each rang with variable called "temp_list"

    #print(temp_movie.head())
    genre = temp_movie.sum().sort_values(ascending=False)
    genre.plot(kind='bar', colormap = 'cool', figsize = (20,8), fontsize =16)

    plt.xlabel("Type of movie")
    plt.ylabel("Number of movie")
    plt.title("Number of movie", fontsize=20)

    plt.show()

    return None


Rate()

runtime()

Classify()