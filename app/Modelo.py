

import pandas as pd


# List of JSON files
files = [
    'yelp_academic_dataset_review.json',
    'yelp_academic_dataset_business.json',
    'yelp_academic_dataset_user.json'
]

# Define the chunk size
chunk_size = 1000  # Adjust this based on your system's memory capacity

# Process each file
for file_name in files:
    # Path to the JSON file
    file_path = file_name  # Adjust if your files are in a specific folder

    # Read the first chunk of the JSON file
    json_reader = pd.read_json(file_path, lines=True, chunksize=chunk_size)
    first_chunk = next(json_reader)

    # Display the columns of the first chunk
    print(f"Columns in {file_name}: {first_chunk.columns.tolist()}")
