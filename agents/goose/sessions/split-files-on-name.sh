#!/bin/bash
# Script to split the memory dump into individual files

# The file containing the memory dump
INPUT_FILE="memory_dump.txt"

# Initialize variables
current_file=""
content=""
capturing=false

# Process the file line by line
while IFS= read -r line; do
  # Check if this line is a header (starts with NAME:)
  if [[ $line == NAME:* ]]; then
    # If we were already capturing content, save it to the current file
    if [ "$capturing" = true ] && [ -n "$current_file" ]; then
      echo "$content" >"${current_file}.txt"
      echo "Created ${current_file}.txt"
    fi

    # Extract the new file name
    base_file=$(echo "$line" | cut -d' ' -f2)
    current_file=$base_file

    # Find an available filename
    counter=1
    while [ -f "${current_file}.txt" ]; do
      current_file="${base_file}-${counter}"
      ((counter++))
    done

    # Reset content
    content=""
    capturing=true
  elif [ "$capturing" = true ]; then
    # Append this line to the content
    if [ -n "$content" ]; then
      content+=$'\n'
    fi
    content+="$line"
  fi
done <"$INPUT_FILE"

# Don't forget the last file
if [ "$capturing" = true ] && [ -n "$current_file" ]; then
  echo "$content" >"${current_file}.txt"
  echo "Created ${current_file}.txt"
fi

echo "All files created successfully!"
