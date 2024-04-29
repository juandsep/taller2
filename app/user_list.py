import json

# List to hold user_ids
user_ids = []

# Open the JSON file and read data
with open('yelp_academic_dataset_user.json', 'r') as file:
    # Assuming the file contains multiple JSON objects, one per line
    for line in file:
        data = json.loads(line)  # Load JSON data from a line
        user_ids.append(data['user_id'])  # Access the user_id and append to the list

# Now user_ids list contains all user_ids from the JSON file
print(user_ids[:10])  # Print first 10 user_ids to check