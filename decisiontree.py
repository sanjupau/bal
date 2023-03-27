import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


data= pd.read_csv("humiduty.csv")

data.columns
data


data.shape
del data['Water']
data.shape

data.shape
clean_data= data.copy()
clean_data['enjoyspot'] = (clean_data['Humidity']>23)*1
clean_data['enjoyspot']
clean_data
y=clean_data['enjoyspot'].copy()
y.columns
y

other_features =['Sky','AirTemp','Wind','Forecast']
x=clean_data[other_features].copy()
x.columns
y.columns
X_train, Y_train, X_test, Y_test = train_test_split(x,y,test_size=0.33, random_state= 324)
y_predicted = humanity.predict(X_test)
accuracy_score(Y_test,y_predicted)*100
