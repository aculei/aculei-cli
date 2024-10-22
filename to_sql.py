import os
import time
from sqlalchemy import create_engine
import pandas as pd

if not os.path.exists('aculei.csv'):
    print('aculei.csv not found')
    exit(1)

df = pd.read_csv('aculei.csv')

username = 'admin'
password = 'admin'
host = 'localhost'
database = 'postgres'

conn_url = f"postgresql://{username}:{password}@{host}:5432/{database}"
engine = create_engine('postgresql://admin:admin@localhost:5432/postgres')

start_time = time.time()

df.to_sql(
    name="aculei",
    con=engine,
    if_exists="append",
    index=False
)

end_time = time.time()
total_time = end_time - start_time
print(f"Insert time: {total_time} seconds")
