import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

excel_file = BASE_DIR/'data'/'raw'/'Dataset for Data Analytics.xlsx'

df = pd.read_excel(excel_file)

processed_dir = BASE_DIR/'data'/'processed'
processed_dir.mkdir(exist_ok=True)

df.to_csv(processed_dir/'cleaned_data.csv', index=False)

print("Shape:", df.shape)
print(df.describe(include='all'))

viz_dir = BASE_DIR/'visualizations'
viz_dir.mkdir(exist_ok=True)

num_cols = df.select_dtypes(include='number').columns

if len(num_cols):
    plt.figure()
    df[num_cols[0]].hist()
    plt.title(num_cols[0])
    plt.savefig(viz_dir/'histogram.png')
    plt.close()

print("EDA Completed")
