import pandas as pd 

data = {
    "name": ['A','B','C'],
    "math": [80,90,100],
    "science":[100,90,80]
}

df = pd.DataFrame(data)
#print(df)
#print(df["math"])
#print(df.iloc[1])

# filtering

highscores = df[df['math']>85]
#print(highscores)

print(df.mean(numeric_only=True))
print(df.describe)