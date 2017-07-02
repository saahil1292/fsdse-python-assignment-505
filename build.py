import pandas as pd


def load_data():
    df = pd.read_csv("/home/saahil1292/Workspace/code/fsdse-python-assignment-505/files/olympics.csv", skiprows=1)
    old_names = ["01 !", "02 !", "03 !"]
    new_names = ["Gold", "Silver", "Bronze"]
    df.rename(columns = dict(zip(old_names, new_names)), inplace=True)
    # df["01 !"] == df["Gold"]
    country_names = [x.split('\xc2\xa0(')[0] for x in df['Unnamed: 0']]
    df.set_index(pd.Series(country_names), inplace=True)
    df.rename(columns={"Unnamed: 0" : "Country"}, inplace=True)
    # df.iloc[:,0] == country_names
    df.drop(["Totals"], axis=0, inplace=True)
    return df

def first_country(df):
    return df.iloc[0,:]


def gold_medal(df):
    return df['Gold'].argmax()


def biggest_difference_in_gold_medal(df):
    df['Difference'] = df['Gold'] - df['01 !.1']
    # df['Difference']
    return df['Difference'].argmax()

def get_points(df):
    df['Points'] = (3 * df.iloc[:,12]) + (2 * df.iloc[:,13]) + (df.iloc[:,14])
    return df['Points']


# df = load_data()
# print(first_country(df)["# Summer"])
# print(gold_medal(df))
# print(biggest_difference_in_gold_medal(df))
# print(get_points(df))
