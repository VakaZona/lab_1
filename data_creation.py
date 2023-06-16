from faker import Faker
import pandas as pd


def generateData(n):
    df = pd.DataFrame(
        [
            {
                "Date": fake.date_this_century(),
                "Time": fake.time(),
                "Temperature": 0,
                "Precipitation_procent": fake.pyint(min_value=0, max_value=100, step=10)
            }
            for _ in range(n)
        ]
    )
    return df


def saveData(df, path):
    df.to_csv(path, index=False)

fake = Faker("ru_Ru")

df_train = generateData(1000)
saveData(df_train, 'train/train.csv')
df_test = generateData(300)
saveData(df_test, 'test/test.csv')
