import os
import json

from groq import Groq

def load_stories(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)[:10]  # Load and return the first 10 stories

# Initialize the Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Path to your JSON file containing stories
file_path = 'cleaned_cns_maryland_posts.json'
stories = load_stories(file_path)

# Iterate over the stories and ask the model to identify entities
for story in stories:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"For each story, identify the people, places, and organizations in the following text: {story['content']}, returning only a JSON object with the following keys: story ( {story['id']}, type (either a person, place or organization) and value (the actual thing). No yapping.",
            }
        ],
        model="llama3-70b-8192",
    )
    # Print the result for each story
    print(chat_completion.choices[0].message.content)
