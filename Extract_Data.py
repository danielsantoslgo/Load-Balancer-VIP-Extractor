import re
import csv

def extract_vip_data(input_file, output_file):
    """
    Extracts VIP names and IP addresses from the input file and writes them into a CSV file.
    :param input_file: Path to the file containing raw data.
    :param output_file: Path to the output CSV file.
    """
    # Define the regex pattern to find vsvip blocks
    vsvip_pattern = re.compile(r"vsvip\s+(\w+).*?IP\s*:\s*(\d+\.\d+\.\d+\.\d+)", re.DOTALL)

    try:
        # Read raw data from the input file
        with open(input_file, 'r') as file:
            raw_data = file.read()

        # Find all matches in the raw data
        matches = vsvip_pattern.findall(raw_data)

        if matches:
            # Write matches to a CSV file
            with open(output_file, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                # Write the header
                csv_writer.writerow(["VIP Name", "IP Address"])
                # Write the rows
                csv_writer.writerows(matches)

            print(f"Data successfully extracted to {output_file}")
        else:
            print("No VIP data found in the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
input_filename = 'load_balancer_data.txt'  # Input file with raw data
output_filename = 'extracted_vip_data.csv'  # Output CSV file
extract_vip_data(input_filename, output_filename)
