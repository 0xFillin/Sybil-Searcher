import csv

def remove_duplicates_from_combined_csv(combined_csv_file, addresses_to_remove_file, output_file):
    with open(addresses_to_remove_file, 'r') as f:
        addresses_to_remove = set(line.strip() for line in f)

    removed_duplicates = 0

    with open(combined_csv_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = next(reader)
        writer.writerow(header)
        address_index = header.index('address')

        for row in reader:
            if row[address_index] not in addresses_to_remove:
                writer.writerow(row)
            else:
                removed_duplicates += 1

    print(f"Duplicates removed: {removed_duplicates}")

if __name__ == "__main__":
    combined_csv_file = 'data.csv'
    addresses_to_remove_file = 'initialList.txt'
    output_file = 'filtered_data.csv'
    remove_duplicates_from_combined_csv(combined_csv_file, addresses_to_remove_file, output_file)

