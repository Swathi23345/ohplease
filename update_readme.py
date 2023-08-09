import json

# Load JSON data
with open('C:\Users\v-rvs\Desktop\AML\data.json', 'r') as json_file:
    json_data = json.load(json_file)

# Generate table content
table_content = "| Key | Value |\n| --- | --- |\n"
for key, value in json_data.items():
    table_content += f"| {key} | {value} |\n"

# Read and update README
with open('README.md', 'r') as readme_file:
    readme_content = readme_file.read()

# Replace placeholder with table content
readme_content = readme_content.replace('<!-- JSON_TABLE -->', table_content)

with open('README.md', 'w') as readme_file:
    readme_file.write(readme_content)
