```markdown

# Load Balancer VIP Extractor

A powerful Python script that does exactly this: it takes raw data from a file and pulls out key information—specifically VIP names and IP addresses from a Load Balancer—and exports it into a CSV file (like a mini spreadsheet).

## Features

- Parses raw data for "vsvip" blocks.
- Extracts VIP names and corresponding IP addresses.
- Outputs the extracted data into a clean CSV file.
- Uses only standard Python modules (`re` and `csv`).

## Example Input File

```
vsvip VIP1
  IP : 192.168.1.1

vsvip VIP2
  IP : 10.0.0.5

Some irrelevant text...

vsvip VIP3
  IP : 172.16.0.2
```

## Example Output CSV

```
VIP Name,IP Address
VIP1,192.168.1.1
VIP2,10.0.0.5
VIP3,172.16.0.2
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/danielsantoslgo/Balancer-VIP-Extractor.git
   cd Balancer-VIP-Extractor


2. Ensure you have Python 3 installed.

## Usage

1. Prepare your input file (e.g., `load_balancer_data.txt`).
   
2. Run the script:
   
   ```bash
   
   python Extract_Data.py
   
   ```

5. Enter the input and output file paths when prompted, or modify the script to use default paths.

## Script Overview

The script uses regular expressions to identify `vsvip` blocks and their associated IP addresses in the raw data. It writes the extracted information into a CSV file with the following structure:

| VIP Name | IP Address  |
|----------|-------------|
| VIP1     | 192.168.1.1 |
| VIP2     | 10.0.0.5    |

## Contributions

Contributions are welcome! Please follow these steps:

1. Fork the repository.
   
2. Create a new branch:
   
   ```bash
   git checkout -b feature-name
   ```
   
3. Commit your changes:
   
   ```bash
   git commit -m "Description of feature"
   ```
   
4. Push to your fork and create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


