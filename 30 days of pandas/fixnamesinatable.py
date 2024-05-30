import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    # capitalize first letter for all the names in the 'name' column
    users['name'] = users['name'].str.capitalize()

    #sort the values in ascending order by user_id
    one = users.sort_values(by='user_id', ascending=True)

    return one