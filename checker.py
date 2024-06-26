import json
import os

# Load the provided cityBackgroundVariables.json file from the current directory
with open("cityBackgroundVariables.json") as f:
    city_background_data = json.load(f)


# Function to load the first JSON file content in a directory
def load_first_json_in_directory(directory):
    dir_path = os.path.join("data", directory)
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        for file in os.listdir(dir_path):
            if file.endswith(".json"):
                file_path = os.path.join(dir_path, file)
                with open(file_path, "r") as f:
                    return json.load(f)
    return None


# Function to check if a value exists in a JSON file's "name" array
def check_value_in_json(directory, value):
    json_content = load_first_json_in_directory(directory)
    if json_content and isinstance(json_content, list):
        return any(entry.get("name") == value for entry in json_content)
    return False


# Results dictionary to store the check results
results = {}

# Check each item in the cityBackground array
for item in city_background_data["cityBackground"]:
    item_id = item["itemId"]
    variables = item["variables"]

    # Check each variable key and value
    variable_results = {}
    for key, value in variables.items():
        directory = key.lower()
        value_exists = check_value_in_json(directory, value)
        variable_results[key] = value_exists

    # Store the results
    results[item_id] = variable_results

# Print the results in a readable format
for item_id, checks in results.items():
    print(f"{item_id}:")
    for key, exists in checks.items():
        print(f"  {key}: {'Exists' if exists else 'Does not exist'}")

# If you want to save the results to a file, uncomment the following lines:
# with open('validation_results.json', 'w') as f:
#     json.dump(results, f, indent=2)
