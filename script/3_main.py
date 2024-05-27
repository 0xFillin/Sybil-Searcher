import os
import csv

def combine_csv_files(input_directory, output_file):
    csv_files = [f for f in os.listdir(input_directory) if f.endswith('.csv')]

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        header_written = False

        for filename in csv_files:
            file_path = os.path.join(input_directory, filename)
            with open(file_path, 'r') as infile:
                reader = csv.reader(infile)
                header = next(reader)

                if not header_written:
                    writer.writerow(['file_name'] + header)
                    header_written = True

                for row in reader:
                    writer.writerow([filename] + row)

if __name__ == "__main__":
    input_directory = './data'
    output_file = 'data.csv'
    combine_csv_files(input_directory, output_file)
