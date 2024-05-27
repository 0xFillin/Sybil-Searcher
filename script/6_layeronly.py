import pandas as pd

def find_similar_addresses(address_count_file, merged_csv_file, output_file):
    address_count_df = pd.read_csv(address_count_file)
    merged_df = pd.read_csv(merged_csv_file)
    merged_df['address'] = merged_df['address'].str.lower()
    merged_df = merged_df.merge(address_count_df, on='address', how='inner')
    merged_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    address_count_file = 'Snapshot#1.csv'
    merged_csv_file = 'merged.csv'
    output_file = 'layer.csv'
    find_similar_addresses(address_count_file, merged_csv_file, output_file)
