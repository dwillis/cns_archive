#!/bin/bash

# Define paths to your files and the database
DATABASE="cns_stories.db"
JSON_FILE="cleaned_cns_maryland_posts.json"
TAGS_CSV="story_tags.csv"
COAUTHORS_CSV="coauthors.csv"

# Check if sqlite-utils is installed and install it if it isn't
if ! command -v sqlite-utils &> /dev/null
then
    echo "sqlite-utils could not be found, attempting to install..."
    pip install sqlite-utils
fi

# Import JSON data into the stories table
sqlite-utils insert $DATABASE stories $JSON_FILE --pk=id

# Import CSV data into the story_tags table
sqlite-utils insert $DATABASE story_tags $TAGS_CSV --csv --detect-types

# Import CSV data into the story_authors table
sqlite-utils insert $DATABASE story_authors $COAUTHORS_CSV --csv --detect-types

sqlite-utils add-foreign-key $DATABASE story_authors story_id stories id
sqlite-utils add-foreign-key $DATABASE story_tags story_id stories id

# Create a Full-Text Search (FTS) table on the stories table for content and excerpt columns
sqlite-utils enable-fts $DATABASE stories content excerpt --fts5

echo "Data import complete. Foreign keys and Full-Text Search have been set up."
