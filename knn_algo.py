#sklearn kaggle UCI

import sklearn as sk
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier

#visualisation
from sklearn.tree import export_graphviz

#sk.datasets.load_iris()

#sk.datasets.fetch_20newsgroups(data_home=None,subset='train')


"""
print("data set(数据集）: \n", iris)
print("description(数据集描述）: \n", iris["DESCR"])
print("feature_name(特征值名字）: \n", iris.feature_names)
print("feature(特征值）: \n", iris.data, iris.data.shape)
print("traget （目标值）: \n", iris.target)
print("traget_names（目标值名字）: \n", iris.target_names)
"""




def knn_irs():

    iris = load_iris()

#数据集的划分

    x_train,x_test,y_train,y_test = train_test_split(iris.data, iris.target, test_size=0.2,random_state=6)
    print("训练集特征值:\n", x_train, x_train.shape)

# one hot encoding
#3标准化

    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

#4KNN算法预估器

    estimator = KNeighborsClassifier(n_neighbors=3)
    estimator.fit(x_train,y_train)

#5模型评估
#方法一，直接对比预测值和实际值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n" , y_predict)
    print("compare the Actual value and predicted value\n", y_test == y_predict)
#方法2，算准确率

    score_accuracy = estimator.score(x_test,y_test)
    print("accurary=\n",score_accuracy)

    return None

#决策树预估器

def decsion_iris():

    #1获取数据集
    iris = load_iris()

    #2 划分数据集
    x_train,x_test,y_train,y_test = train_test_split(iris.data, iris.target, test_size=0.2,random_state=6)

    #3决策树预估器
    estimator = DecisionTreeClassifier(criterion="entropy")
    estimator.fit(x_train,y_train)

    #4) 模型评估

#5模型评估
#方法一，直接对比预测值和实际值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n" , y_predict)
    print("compare the Actual value and predicted value\n", y_test == y_predict)
#方法2，算准确率

    score_accuracy = estimator.score(x_test,y_test)
    print("accurary=\n",score_accuracy)

    export_graphviz(estimator, out_file="iris_tree.dot",feature_names=iris.feature_names)
    print("visit webgraphviz.com to create a graphic, you just need to copy the texte in the iris_tree.dot and paste it on the page")

    return None


decsion_iris()
knn_irs()