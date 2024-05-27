import pandas as pd

input_file = 'layer.csv'
df = pd.read_csv(input_file)

address_counts = df['to'].value_counts()

filtered_df = df[df['to'].isin(address_counts[address_counts >= 20].index)]

output_file = 'general.csv'
filtered_df.to_csv(output_file, index=False)

print(f"Saved in: {output_file}")