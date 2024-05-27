import os
import csv
import re

def wei_to_eth(value):
    return float(value) / 10**18

def find_wallet_addresses(folder_path):
    wallet_addresses = set()
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                data = file.read()
                addresses = re.findall(r'0x[0-9a-fA-F]{40}', data)
                wallet_addresses.update(addresses)
    return wallet_addresses

def compare_and_save(wallet_addresses, csv_file_path, output_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open(output_file_path, 'w', newline='') as output_file:
            fieldnames = ['address', 'to', 'value']
            csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for row in csv_reader:
                if row['address'] in wallet_addresses:
                    row['value'] = wei_to_eth(int(row['value']))
                    csv_writer.writerow(row)

data_folder = 'data'
csv_file_path = 'decoded_transactions.csv'
output_file_path = 'matched_transactions.csv'

wallet_addresses = find_wallet_addresses(data_folder)
compare_and_save(wallet_addresses, csv_file_path, output_file_path)

print("saved matched_transactions.csv")