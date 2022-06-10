import numpy as np
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt

'''
读取数据并储存于变量（？）中
'''
prices_pd = pd.read_csv("Weed_Price.csv")
demography_pd = pd.read_csv("Demographics_State.csv")
population_pd = pd.read_csv("Population_State.csv")



# type de prices_pd:
#print(type(prices_pd))
# type de demography_pd
#print(type(demography_pd))
# type de population_pd
#print(type(population_pd))


# 15 premières lignes de prices_pd

'''
打印某个文件中的前十五行，后十五行
'''
#print(prices_pd.head(15))

#print(population_pd.tail(15))


'''
选取并打印某个文件中包含某种条件的行，并可抓取特定的列，比如这里是选取了所有state为hawaii的行，并打印出了"date","HighQ", "MedQ"三列
'''
# Les lignes concernant l'état "Hawaii"
#print(prices_pd.loc[prices_pd['State'] == 'Hawaii'])

# Les valeurs de la colonne "HighQ" ne concernant que les lignes de l'état "Hawaii"
#print(prices_pd.loc[prices_pd['State'] == 'Hawaii',["date","HighQ", "MedQ"]])

#prices_pd.dtypes
'''
单独打印出文件中的某一类数据（比如这里是打印出所有state的名字），且不重复
'''

#les_etats = np.unique(prices_pd["State"].values)
# Afficher la liste des états :
#print(les_etats)

'''打印出MedQ有多少列，第一个未取消重复值，第二个取消了重复值（应该是单元格中数值相同的部分'''
#print(prices_pd["MedQ"].values.size)
#print(np.unique(prices_pd["MedQ"].values).size)


'''对数据进行操作'''


''' 求平均值 '''
#先写一个函数
def moyenne(tab):
    taille = tab.size #确定样本总量，用size
    sum = 0 #设初始变量值为0
    for i in range (0,taille): #设一个循环的for函数，从0加到样本总量
        sum += tab[i]   #从单元格的第0个数开始，一直加到最后一个
    return sum /taille

"""将MEDQ的这一列单独打出来"""
#print(prices_pd["MedQ"])


"""打印出平均值，然后我们发现其实用mean函数也可以直接得到结果"""
#print("La moyenne (MedQ) est avec ma fonction : %f dollars" % moyenne(prices_pd["MedQ"]))
#print("La moyenne (MedQ) est avec mean        : %f dollars" % prices_pd["MedQ"].mean())

"打印其他的平均值，我们甚至可以用loc和meas来特定选取带有某些属性的数值"
#print("La moyenne (MedQ) est : %f dollars" % moyenne(prices_pd["MedQ"]))
#print("La moyenne (HighQ) est : %f dollars" % prices_pd["HighQ"].mean())
#print("La moyenne (HighQ) à NY: %f dollars" % prices_pd.loc[prices_pd['State'] == "New York", ["HighQ"]].mean())
#print("La moyenne (MedQ) à NY : %f dollars" % prices_pd.loc[prices_pd['State'] == "New York", ["MedQ"]].mean())


'打印直方图'
'''# Par exemple, tracé de l'histograme des valeurs "LowQ" sur l'ensemble des données:
plt.hist(prices_pd["LowQ"])

plt.show()

prix_moyens=prices_pd[["State","LowQ"]].groupby(["State"]).mean()
#print(prix_moyens)
#print("===========")
prix_moyens=prix_moyens.values.ravel()

plt.hist(prix_moyens)

plt.show()'''



prix_ny=prices_pd[prices_pd['State']=='New York']
prix_ca=prices_pd[prices_pd['State']=='California']
prix_ca_ny=prix_ca.merge(prix_ny,on='date')
prix_ca_ny.head()



'我们将两类数据合并，然后进行相关性分析'
