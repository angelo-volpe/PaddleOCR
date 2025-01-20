import yaml
import argparse


parser = argparse.ArgumentParser(description="Update YAML with a fine-tuning dataset path.")
parser.add_argument("--fine_tuning_dataset_path", required=True, help="Path to the fine-tuning dataset")
parser.add_argument("--document_id", required=True, help="id of document to process")
args = parser.parse_args()

fine_tuning_dataset_path = args.fine_tuning_dataset_path
document_id = args.document_id

with open("./configs/det/document_fine_tuning.yml", "r") as yaml_file:
    data = yaml.safe_load(yaml_file.read())

# Recursively replace placeholders in the dictionary
def replace_placeholders(obj, replacements):
    if isinstance(obj, dict):
        return {k: replace_placeholders(v, replacements) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_placeholders(i, replacements) for i in obj]
    elif isinstance(obj, str):
        # Replace placeholders in strings
        for key, value in replacements.items():
            obj = obj.replace(f"${{{key}}}", value)
        return obj
    return obj

# Perform the replacement
replacements = {"fine_tuning_dataset_path": fine_tuning_dataset_path, "document_id": document_id}
updated_data = replace_placeholders(data, replacements)

with open(f"./configs/det/document_{document_id}_fine_tuning.yml", "w") as outfile:
    yaml.dump(updated_data, outfile)
