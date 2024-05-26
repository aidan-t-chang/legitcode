import pandas as pd

def invalid_tweets(tweets) -> pd.DataFrame:
    dfa = tweets[tweets['content'].str.len() > 15]
    df = dfa.iloc[:, [0]]
    return df