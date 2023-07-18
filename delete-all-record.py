import requests
import json

def bulk_delete_dns_records(zone_id, email, api_key):
    base_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": email,
        "X-Auth-Key": api_key
    }

    deleted_records = []

    response = requests.get(base_url, headers=headers)
    data = response.json()

    if response.status_code == 200 and data["success"]:
        records = data["result"]

        for record in records:
            record_id = record["id"]
            delete_url = f"{base_url}/{record_id}"

            delete_response = requests.delete(delete_url, headers=headers)
            delete_data = delete_response.json()

            if delete_response.status_code == 200 and delete_data["success"]:
                deleted_records.append(record["name"])

    return deleted_records

# Prompt for Cloudflare credentials
zone_id = input("Enter your Cloudflare Zone ID: ")
email = input("Enter your Cloudflare email: ")
api_key = input("Enter your Cloudflare API key: ")

deleted_records = bulk_delete_dns_records(zone_id, email, api_key)

print("Deleted records:")
for record_name in deleted_records:
    print(record_name)
