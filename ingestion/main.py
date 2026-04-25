import pandas as pd
from google.cloud import bigquery
from config.config import PROJECT_ID, RAW_DATASET, SOURCES

client = bigquery.Client()

def load_to_bq(table_name, url):
    try:
        print(f"Processing {table_name}...")

        df = pd.read_csv(url)
        print(f"{table_name} rows: {len(df)}")

        df.columns = df.columns.str.lower().str.replace(" ", "_")

        table_id = f"{PROJECT_ID}.{RAW_DATASET}.{table_name}"
        print(f"Loading to {table_id}")

        job = client.load_table_from_dataframe(df, table_id)
        job.result()

        print(f"SUCCESS: {table_name}")

    except Exception as e:
        print(f"ERROR in {table_name}: {e}")

def main():
    print("START INGESTION")
    for table, url in SOURCES.items():
        load_to_bq(table, url)

    print("DONE")

if __name__ == "__main__":
    main()
