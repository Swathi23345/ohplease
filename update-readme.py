import json
import pandas as pd
import yaml
with open('runs_json.json') as json_data:
    data_json = json.load(json_data)

df=pd.DataFrame(data_json)
dict_df = pd.DataFrame(df['workflow_runs'].tolist())
dict_df = dict_df[["id","name","conclusion","run_attempt"]]
req_json=dict_df.to_dict(orient='records')
yaml_string = yaml.dump(req_json)
with open('runs.yaml', 'w+') as f:
    f.write(yaml_string)
with open('runs.yaml') as runyaml:
    runyaml =yaml.safe_load(runyaml)
# Generate Markdown table
markdown_table = "| id | name | conclusion | run_attempt |\n| -- | ---- | ---------- | ----------- |\n"
for item in runyaml:
    markdown_table += f"| {item['id']} | {item['name']}  | {item['conclusion']} | {item['run_attempt']} | \n"

# Write Markdown table to file
# with open("test.md", "w") as md_file:
#     md_file.write(markdown_table)
# output = ""
# with open("test.md", "r") as readme_file:
#     output = readme_file.read()

# update_readme.py

def generate_markdown():
    # Replace this with your actual code to generate Markdown
    return markdown_table

def update_readme(readme_path, marker):
    generated_markdown = generate_markdown()

    with open(readme_path, "r") as readme_file:
        readme_content = readme_file.read()

    updated_readme_content = readme_content.replace(marker, generated_markdown)

    with open(readme_path, "w") as readme_file:
        readme_file.write(updated_readme_content)

if __name__ == "__main__":
    readme_file_path = "https://github.com/Swathi23345/ohplease/blob/main/README.md"
    content_marker = "<!-- GENERATED_CONTENT_MARKER -->"
    update_readme(readme_file_path, content_marker)


