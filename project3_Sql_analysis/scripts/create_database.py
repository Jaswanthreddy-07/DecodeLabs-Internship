import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
df = pd.read_excel(BASE_DIR/'data'/'raw'/'Dataset for Data Analytics.xlsx')

conn = sqlite3.connect(BASE_DIR/'data'/'database'/'analytics.db')
df.to_sql('dataset', conn, if_exists='replace', index=False)
conn.close()

print('Database created successfully')
