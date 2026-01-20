import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def dataCleaning():
    df = pd.read_csv(r"C:\Users\Tena\Documents\Python proj\Data Cleaning\Customer Call List.csv")

    df = df.drop_duplicates()

    df = df.drop(columns="Not_Useful_Column")

    df["Last_Name"] = df["Last_Name"].str.strip("123._/")

    df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]', "")

    df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))

    df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

    df["Phone_Number"] = df["Phone_Number"].str.replace("nan--", "")

    df["Phone_Number"] = df["Phone_Number"].str.replace("Na--", "")

    df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(",", expand=True) 

    df["Paying Customer"] = df["Paying Customer"].str.replace("Yes", "Y")

    df["Paying Customer"] = df["Paying Customer"].str.replace("No", "N")

    df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes", "Y")

    df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No", "N")

    df = df.replace("N/a", "")

    df = df.replace("NaN", "")

    df = df.fillna("")

    for x in df.index:
        if df.loc[x, "Do_Not_Contact"] == "Y":
            df.drop(x, inplace=True)
        
    for x in df.index:
        if df.loc[x, "Phone_Number"] == "":
            df.drop(x, inplace=True)

    df = df.reset_index(drop=True)

    sns.scatterplot(data=df, x="Paying Customer", y="Do_Not_Contact", hue=None)
    
    plt.title("Scatter Plot from CSV Data")
    plt.xlabel("X Axis Label")
    plt.ylabel("Y Axis Label")
    plt.tight_layout()
    plt.show()

dataCleaning()

