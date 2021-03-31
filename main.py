from pac.extraction import Apriori
import pandas as pd


if __name__ == '__main__':
    data = pd.read_csv("base.csv")
    X = data.drop(columns=['classe'])
    y = data['classe']

    apriori = Apriori(0.1, 0.5)
    apriori.fit(X, y)

