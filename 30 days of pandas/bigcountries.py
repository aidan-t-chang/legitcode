import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    data = world[['name', 'population', 'area']]

    only_big = data[(world['population'] >= 25000000) | (world['area'] >= 3000000)]

    return only_big