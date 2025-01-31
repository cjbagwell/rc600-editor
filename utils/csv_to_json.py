import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, newline='') as csvfile:
        # Read the CSV file with headers
        reader = csv.reader(csvfile)
        # Create a dictionary to store the data
        data = {}
        # Loop through the rows in the CSV file
        for row in reader:
            # Get the first column as the key
            key = row[0]
            # Get the second column and split it by commas to create a list of strings
            value = row[1].split(',')
            # Add the key and value to the dictionary
            data[key] = value
    
    # Write the data to a JSON file
    with open(json_file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Example usage
csv_files = [r"C:\Users\cjbag\Downloads\bean_genre_Pattern.csv",
r"C:\Users\cjbag\Downloads\Beat_Genre.csv"]
for file in csv_files:
    csv_to_json(file, file.replace(".csv", ".json"))