import csv

def remove_duplicates_from_combined_csv(combined_csv_file, addresses_to_remove_file, output_file):
    with open(addresses_to_remove_file, 'r') as f:
        addresses_to_remove = set(line.strip().lower() for line in f)

    removed_duplicates = 0

    with open(combined_csv_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        writer.writerow(header)

        try:
            address_index = header.index('to')
        except ValueError:
            print("The 'to' column is not found in the CSV file header.")
            return

        for row in reader:
            if row[address_index].strip().lower() not in addresses_to_remove:
                writer.writerow(row)
            else:
                removed_duplicates += 1

    print(f"Duplicates removed: {removed_duplicates}")

if __name__ == "__main__":
    combined_csv_file = 'filtered_data.csv'
    addresses_to_remove_file = 'cexlist.txt'
    output_file = 'merged.csv'
    remove_duplicates_from_combined_csv(combined_csv_file, addresses_to_remove_file, output_file)
