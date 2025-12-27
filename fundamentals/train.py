from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

data = {
    "hours_studied" : [1,2,3,4,5,6],
    "attendance" : [30,40,50,60,70,80],
    "marks" : [35,45,55,65,75,85]
}

df = pd.DataFrame(data)

#splitting features and labels
df["hours_studied"] = df["hours_studied"] + np.random.randint(-1, 2, size=len(df))
df["attendance"] = df["attendance"] + np.random.randint(-1, 2, size=len(df))

x = df[["hours_studied","attendance"]]
y = df["marks"]
    



df['performance'] = (df['marks']>= 60).map({
    True:'good',
    False:'bad'
})

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2,random_state=42
)

model = LinearRegression()
model.fit(x_train,y_train)

train_score = model.score(x_train,y_train)
test_score = model.score(x_test,y_test)

print(train_score,test_score)

y_pred = model.predict(x_test)
mse = mean_squared_error(y_test,y_pred)

print(mse)