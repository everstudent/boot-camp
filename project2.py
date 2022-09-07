import pandas as pd

# 1. load & describe data
data = pd.read_csv('./data.csv');
print(data.info())
print(data.describe())



# 2. Convert categorial features to numeric
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

data['LUNG_CANCER'] = le.fit_transform(data['LUNG_CANCER'])
data = pd.get_dummies(data, columns = ['GENDER'])

y = data['LUNG_CANCER']
data = data.loc[:, data.columns!='LUNG_CANCER']



# 3. Normalize data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
data = pd.DataFrame(sc.fit_transform(data), columns = data.columns)
print(data.head())



# 4. Split set
from sklearn.model_selection import train_test_split
x = data
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=0)



# 5. Train model
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

lr = LogisticRegression()
lr.fit(x_train, y_train)
lr_pred = lr.predict(x_test)
lr_report = classification_report(y_test, lr_pred)
lr_acc = round(accuracy_score(y_test, lr_pred)*100, ndigits=2)

print('=== RESULTS ===')
print(lr_report)
print(lr_acc)
