import json
import csv

def extract_to_csv(input_file):
    # Load JSON data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Initialize counters for unique IDs
    tag_id_counter = 1
    author_id_counter = 1

    # Prepare to write tag data to CSV
    with open('story_tags.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'story_id', 'tag_id'])  # Write headers with added 'id' column

        for item in data:
            story_id = item['id']
            tags = item.get('tags', [])
            for tag in tags:
                writer.writerow([tag_id_counter, story_id, tag])  # Include the sequential ID
                tag_id_counter += 1  # Increment ID

    # Prepare to write coauthor data to CSV
    with open('coauthors.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'story_id', 'author_id'])  # Write headers with added 'id' column

        for item in data:
            story_id = item['id']
            coauthors = item.get('coauthors', [])
            for author_id in coauthors:
                writer.writerow([author_id_counter, story_id, author_id])  # Include the sequential ID
                author_id_counter += 1  # Increment ID

    print("CSV files for tags and coauthors have been created with sequential IDs.")

# Specify the input file name
input_file = 'cns_maryland_posts.json'

# Extract data and write to CSV files
extract_to_csv(input_file)
