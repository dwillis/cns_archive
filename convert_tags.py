import json
import csv

# Path to the JSON file and the output CSV file
json_file_path = 'tags.json'
csv_file_path = 'tags.csv'

def convert_json_to_csv(json_fp, csv_fp):
    # Read the JSON data
    with open(json_fp, 'r') as file:
        tags_data = json.load(file)
    
    # Create and write to the CSV file
    with open(csv_fp, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        # Write the header
        csv_writer.writerow(['id', 'count', 'link', 'name', 'slug'])
        
        # Write the data rows
        for tag in tags_data:
            # Extract each piece of data based on the specified headers
            id_value = tag.get('id', '')
            count_value = tag.get('count', '')
            link_value = tag.get('link', '')
            name_value = tag.get('name', '')
            slug_value = tag.get('slug', '')
            
            # Write the data to the CSV
            csv_writer.writerow([id_value, count_value, link_value, name_value, slug_value])

    print(f"Data has been written to {csv_fp}")

# Call the function with the file paths
convert_json_to_csv(json_file_path, csv_file_path)
