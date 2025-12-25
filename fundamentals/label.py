import pandas as pd

data = {
    "hours_studied" : [1,2,3,4,5,6],
    "attendance" : [30,40,50,60,70,80],
    "marks" : [35,45,55,65,75,85]
}

df = pd.DataFrame(data)

#splitting features and labels

x = df[["hours_studied","attendance"]]
y = df["marks"]
    
#print(x)
#print(y)

df['performance'] = (df['marks']>= 60).map({
    True:'good',
    False:'bad'
})

print(df)