import pandas as pd


def import_data(file):
    df = pd.read_csv(file)
    dis = list(df['DISTANCE'])
    height = list(df['HEIGHT'])
    return dis, height

