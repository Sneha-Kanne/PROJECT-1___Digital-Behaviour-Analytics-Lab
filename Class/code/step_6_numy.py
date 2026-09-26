import pandas as pd

df = pd.read_csv("digital_behaviour.csv")

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDescription:")
print(df.describe())

print("\nInstagram Minutes:")
print(df["Instagram_Minutes"])

print("\nDate and Instagram Minutes:")
print(df[["Date", "Instagram_Minutes"]])

print("\nTotal Instagram time:")
print(df["Instagram_Minutes"].sum())

print("\nAverage Study time:")
print(df["Study_Minutes"].mean())

print("\nHeaviest YouTube day:")
print(df["YouTube_Minutes"].max())

print("\nInstagram above 100:")
print(df[df["Instagram_Minutes"] > 100])

print("\nStudy above 180:")
print(df[df["Study_Minutes"] > 180])

print("\nInstagram high and Study low:")
print(df[(df["Instagram_Minutes"] > 100) & (df["Study_Minutes"] < 180)])

print("\nNumber of heavy Instagram days:")
print((df["Instagram_Minutes"] > 100).sum())

print("\nSorted by Instagram, highest first:")
print(df.sort_values("Instagram_Minutes", ascending=False))

print("\nTop 5 Instagram days:")
print(df.sort_values("Instagram_Minutes", ascending=False).head(5))

print("\nFive best Study days:")
print(df.sort_values("Study_Minutes", ascending=False).head(5))

df["Total_Screen_Time"] = (
    df["Instagram_Minutes"]
    + df["YouTube_Minutes"]
    + df["WhatsApp_Minutes"]
    + df["LinkedIn_Minutes"]
)

df["Screen_Hours"] = (df["Total_Screen_Time"] / 60).round(2)

df["Digital_Balance"] = (
    df["Study_Minutes"] / df["Total_Screen_Time"]
).round(4)

df["Day_Type"] = df["Total_Screen_Time"].apply(
    lambda x: "Heavy" if x > 300 else "Normal"
)

print("\nTotal minutes by app:")
print(df[["Instagram_Minutes", "YouTube_Minutes", "WhatsApp_Minutes", "LinkedIn_Minutes"]].sum())

print("\nApp with the most total time:")
print(df[["Instagram_Minutes", "YouTube_Minutes", "WhatsApp_Minutes", "LinkedIn_Minutes"]].sum().idxmax())

print("\nNumber of Heavy days:")
print((df["Day_Type"] == "Heavy").sum())

print("\nBest study day:")
print(df.loc[df["Study_Minutes"].idxmax(), ["Date", "Study_Minutes"]])

heaviest_day = df["Total_Screen_Time"].idxmax()
print("\nStudy on heaviest screen day:")
print(df.loc[heaviest_day, ["Date", "Study_Minutes", "Total_Screen_Time"]])

print("\nAverage Digital Balance:")
print(df["Digital_Balance"].mean())

df.to_csv("my_analysis.csv", index=False)

print("\nmy_analysis.csv created successfully.")
