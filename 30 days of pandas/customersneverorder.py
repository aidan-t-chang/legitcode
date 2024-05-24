import pandas as pd # type: ignore

def find_customers(customers, orders):

    #boolean indexing to filter rows from the "customers" dataframe
    df = customers[~customers['id'].isin(orders['customerId'])]
    
    #build the dataframe
    df = df[['name']].rename(columns={'name': 'Customers'})
    return df