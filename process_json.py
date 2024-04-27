import json
from bs4 import BeautifulSoup

def clean_html(raw_html):
    """
    Function to strip HTML tags from strings, ensuring non-empty strings are processed.
    """
    if raw_html and isinstance(raw_html, str):  # Ensure the input is a non-empty string
        soup = BeautifulSoup(raw_html, "html.parser")
        return soup.get_text()
    return ""  # Return an empty string if raw_html is empty or not a string

def process_json_file(input_file, output_file):
    # Load JSON data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Keys to remove from each JSON object
    keys_to_remove = ["guid", "modified_gmt", "template", "meta", "categories", "tags", "coauthors", 
                      "jetpack_publicize_connections", "parsely", "jetpack_featured_media_url", 
                      "jetpack_shortlink", "jetpack_sharing_enabled", "_links", "curies"]

    cleaned_data = []

    for item in data:
        # Remove specified keys
        for key in keys_to_remove:
            item.pop(key, None)
        
        # Process protected attributes to only contain the 'rendered' value
        for key in ['title', 'content', 'excerpt']:
            if key in item and 'rendered' in item[key]:
                item[key] = clean_html(item[key]['rendered'])

        cleaned_data.append(item)

    # Save the cleaned data to a new JSON file
    with open(output_file, 'w') as file:
        json.dump(cleaned_data, file, indent=4)

    print(f"Processed data saved to {output_file}")

# Specify the input and output file names
input_file = 'cns_maryland_posts.json'
output_file = 'cleaned_cns_maryland_posts.json'

# Process the JSON file
process_json_file(input_file, output_file)
