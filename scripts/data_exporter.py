import pandas as pd

def save_to_csv(data, file_name="twitter_trends.csv"):
    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)
