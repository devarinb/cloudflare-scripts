# Cloudflare DNS Record Management Scripts

This repository contains two Python scripts that interact with the Cloudflare API to manage DNS records in a Cloudflare zone. The scripts provide the following functionality:

- `bulk-add-record.py`: Adds DNS records in bulk to a Cloudflare zone.

- `delete-all-record.py`: Deletes all DNS records from a Cloudflare zone.

## Prerequisites

Before running the scripts, ensure that you have the following prerequisites:

- Python 3 installed on your machine.

- The `requests` library installed. You can install it using the command: `pip install requests`.

## Getting Started

Follow the instructions below to run and use the scripts:

1. Clone the repository to your local machine: `git clone https://github.com/your-username/cloudflare-scripts.git`.

2. Navigate to the cloned directory: `cd cloudflare-scripts`.

## Script: bulk-add-record.py

This script allows you to add multiple DNS records to a Cloudflare zone.

### Usage

1. Open the `bulk-add-record.py` script in a text editor.

2. Update the placeholders with your actual Cloudflare credentials and zone ID.

3. Modify the `dns_records` list with the DNS records you want to add. Each record should be a dictionary with the necessary attributes: type, name, content, and proxied.

4. Save the changes.

### Running the Script

To run the script, open a terminal or command prompt and navigate to the cloned directory. Then, execute the following command:

```shell

python bulk-add-record.py

The script will prompt for the number of DNS records to add, as well as the details of each record (type, name, content, and whether to enable Cloudflare proxy). After providing the required information, the script will add the DNS records to the Cloudflare zone.

Please exercise caution when using this script, as it can modify DNS records in your Cloudflare zone. Make sure to double-check and backup any essential records before running the script.


## **Script: delete-all-record.py**

This script allows you to delete all DNS records from a Cloudflare zone.


### **Usage**



1. Open the `delete-all-record.py` script in a text editor.
2. Update the placeholders with your actual Cloudflare credentials and zone ID.
3. Save the changes.


### **Running the Script**

To run the script, open a terminal or command prompt and navigate to the cloned directory. Then, execute the following command:


```
python delete-all-record.py
```


The script will prompt for confirmation before deleting all DNS records in the Cloudflare zone. Please exercise caution, as this action is irreversible.

Please exercise caution when using this script, as it will delete all DNS records within the specified zone. Make sure to double-check and backup any essential records before running the script.
