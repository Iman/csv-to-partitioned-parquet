import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os

df = pd.read_csv("./data/fake_data.csv")

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['PartitionYear'] = df['Timestamp'].dt.year
df['PartitionMonth'] = df['Timestamp'].dt.month
df['PartitionDay'] = df['Timestamp'].dt.day

table = pa.Table.from_pandas(df)

output_directory = './out'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

parquet_file_path = f"{output_directory}/fake_data_partitioned.parquet"

pq.write_to_dataset(
    table,
    root_path=parquet_file_path,
    partition_cols=['PartitionYear', 'PartitionMonth', 'PartitionDay']
)

print(f"Partitioned Parquet file saved to: {parquet_file_path}")
