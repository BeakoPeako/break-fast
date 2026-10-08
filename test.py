import pandas as pd

df = pd.read_csv("Data/users.csv")

if "aa" in df["username"].astype(str).values:
    passwordd = df.loc[df["username"] == "aa", "password"]
    matched = ("aa" == passwordd)
print(matched == True)