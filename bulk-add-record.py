import requests
import json

def bulk_add_dns_records(zone_id, email, api_key, dns_records):
    base_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": email,
        "X-Auth-Key": api_key
    }

    added_records = []

    for record in dns_records:
        response = requests.post(base_url, headers=headers, data=json.dumps(record))
        data = response.json()

        if response.status_code == 200 and data["success"]:
            added_records.append(record["name"])

    return added_records

# Prompt for Cloudflare credentials
zone_id = input("Enter your Cloudflare Zone ID: ")
email = input("Enter your Cloudflare email: ")
api_key = input("Enter your Cloudflare API key: ")

# Prompt for DNS records
dns_records = []
num_records = int(input("Enter the number of DNS records to add: "))

for i in range(num_records):
    record = {}
    print(f"DNS Record #{i + 1}")
    record["type"] = input("Enter the record type (e.g., A, CNAME): ")
    record["name"] = input("Enter the record name: ")
    record["content"] = input("Enter the record content: ")
    record["proxied"] = input("Enable Cloudflare proxy? (true/false): ").lower() == "true"
    dns_records.append(record)

added_records = bulk_add_dns_records(zone_id, email, api_key, dns_records)

print("Added records:")
for record_name in added_records:
    print(record_name)
