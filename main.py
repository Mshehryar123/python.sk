
import requests
import json




# Define Cloudflare API credentials
api_key = 'aeb831fb178c640e59c0fc61b6353599df919'
email = 'mshehryar@adapture.com'
zone_id = 'aff0080f4ae6d84ab134e9659a295418'

# Common headers for Cloudflare API requests (For Authorization)
headers = {
    'X-Auth-Email': email,
    'X-Auth-Key': api_key,
    'Content-Type': 'application/json',
}

# Function to create a DNS record
def create_dns_record(zone_id, dns_record_data):
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    response = requests.post(url, json=dns_record_data, headers=headers)

    if response.status_code == 200:
        print("DNS record created successfully.")
    else:
        print(f"Error creating DNS record. Status Code: {response.status_code}")
        print("Response:", response.text)

# Function to fetch DNS records
def fetch_dns_records(zone_id):
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        dns_records = response.json()
        print("DNS Records:")
        for record in dns_records["result"]:
            print(f"Type: {record['type']}, Name: {record['name']}, Content: {record['content']}")
    else:
        print(f"Error fetching DNS records. Status Code: {response.status_code}")
        print("Response:", response.text)

# Function to update a DNS record
# Function to update a DNS record
def update_dns_record(zone_id, record_id, updated_data):
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}'
    response = requests.put(url, json=updated_data, headers=headers)

    if response.status_code == 200:
        print("DNS record updated successfully.")
    else:
        print(f"Error updating DNS record. Status Code: {response.status_code}")
        print("Response:", response.text)


# Function to delete a DNS record
def delete_dns_record(zone_id,record_id):
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}'
    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print("DNS record deleted successfully.")
    else:
        print(f"Error deleting DNS record. Status Code: {response.status_code}")
        print("Response:", response.text)



if __name__ == '__main__':

    # all the functions will be called from this main function if any function needs to be commented it needs to be commented here.

    # #  DNS record data for creation
    # dns_record_data = {
    #     'type': 'A',
    #     'name': 'this.com',
    #     'content': '192.168.1.6'
    # }

    # Call the create_dns_record function
    # create_dns_record(zone_id, dns_record_data)

    # Call the fetch_dns_records function to display DNS records
 # fetch_dns_records(zone_id)

    # updated data for updating a DNS record (for updating a DNS record)
    # updated_data = {
    #     'type': 'A',
    #     'name': 'Update.com',
    #     'content': '192.168.1.7'
    # }

    # record_id for updating and deleting a DNS record (this  record_id can be fetched from the record_id.py script)
    record_id = 'aa7c022c819826af920eb7078c285108'

    # Call the update_dns_record function
    # update_dns_record(zone_id, record_id, updated_data)

    # Call the delete_dns_record function
    delete_dns_record(zone_id, record_id)
