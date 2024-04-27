import requests
import json

def fetch_all_tags(base_url):
    page = 1
    all_tags = []

    # Define headers to mimic a Firefox browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
    }

    while True:
        # Construct the URL with the current page number
        page_url = f"{base_url}?page={page}"
        response = requests.get(page_url, headers=headers)

        if response.status_code == 200:
            tags = response.json()
            if not tags:  # Break the loop if the page is empty
                break

            # Process each tag and exclude specific attributes
            for tag in tags:
                if '_links' in tag:
                    del tag['_links']
                if 'curies' in tag:
                    del tag['curies']
                all_tags.append(tag)

            print(f"Page {page} processed.")
            page += 1  # Increment to fetch next page
        else:
            print(f"Failed to retrieve data from page {page}: Status Code {response.status_code}")
            break

    return all_tags

def save_tags_to_json(tags, filename):
    # Save the tags to a JSON file
    with open(filename, 'w') as file:
        json.dump(tags, file, indent=4)
    print(f"Tags have been saved to {filename}")

# URL to fetch tags from
base_url = 'https://cnsmaryland.org/wp-json/wp/v2/tags'
tags = fetch_all_tags(base_url)
save_tags_to_json(tags, 'tags.json')
