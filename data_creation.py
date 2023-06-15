from faker import Faker
import pandas as pd


def generateData(n):
    df = pd.DataFrame(
        [
            {
                "Name": fake.name(),
                "City": fake.city(),
                "Job": fake.job(),
                "Salary": fake.pyint(min_value=10000, max_value=300000, step=5000),
                "Expirience": fake.pyint(min_value=1, max_value=20, step=1)
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
