import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

#visualisation
from sklearn.tree import export_graphviz

from sklearn.model_selection import GridSearchCV #自动调参



from sklearn.ensemble import RandomForestClassifier

def decision_titanic():

    titanic= pd.read_csv("titanic.csv")

    #print(titanic.head())

    x = titanic[["pclass","age","sex"]]
    y = titanic["survived"]

    print(x.head())
    print(y.head())

    "填补缺失值"

    x['age'].fillna(x["age"].mean(),inplace = True)#用年龄平均值填补缺失值

    x = x.to_dict(orient = "records")



    x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=22)

    transfer = DictVectorizer()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    #3决策树预估器
    estimator = DecisionTreeClassifier(criterion="entropy",max_depth=6)
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

    export_graphviz(estimator, out_file="titanic_tree.dot",feature_names=transfer.get_feature_names())
    print("visit webgraphviz.com to create a graphic, you just need to copy the texte in the iris_tree.dot and paste it on the page")

    return None

decision_titanic()

