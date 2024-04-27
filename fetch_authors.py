import requests
import json

def fetch_all_authors(base_url):
    page = 1
    all_authors = []

    # Define headers to mimic a Firefox browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
    }

    while True:
        # Construct the URL with the current page number
        page_url = f"{base_url}?page={page}"
        response = requests.get(page_url, headers=headers)

        if response.status_code == 200:
            authors = response.json()
            if not authors:  # Break the loop if the page is empty
                break

            # Process each author and exclude specific attributes
            for author in authors:
                if '_links' in author:
                    del author['_links']
                if 'curies' in author:
                    del author['curies']
                all_authors.append(author)

            print(f"Page {page} processed.")
            page += 1  # Increment to fetch next page
        else:
            print(f"Failed to retrieve data from page {page}: Status Code {response.status_code}")
            break

    return all_authors

def save_authors_to_json(authors, filename):
    # Save the authors to a JSON file
    with open(filename, 'w') as file:
        json.dump(authors, file, indent=4)
    print(f"Authors have been saved to {filename}")

# URL to fetch authors from
base_url = 'https://cnsmaryland.org/wp-json/wp/v2/coauthors'
authors = fetch_all_authors(base_url)
save_authors_to_json(authors, 'coauthors.json')
