import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
conn = sqlite3.connect(BASE_DIR/'data'/'database'/'analytics.db')

queries = [
    'SELECT COUNT(*) FROM dataset',
    'SELECT AVG(TotalPrice) FROM dataset',
    'SELECT MAX(TotalPrice) FROM dataset',
    'SELECT MIN(TotalPrice) FROM dataset'
]

for q in queries:
    print('\nQuery:', q)
    print(conn.execute(q).fetchall())

conn.close()
