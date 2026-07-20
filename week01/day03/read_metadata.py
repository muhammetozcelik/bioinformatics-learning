import csv


metadata_path = "week01/day03/data/experiment_metadata.csv"
samples = {}

with open(metadata_path, "r") as metadata_file:
    reader = csv.DictReader(metadata_file)

    for row in reader:
        sample_id = row["sample_id"]
        condition = row["condition"]
        replicate = int(row["replicate"])

        samples[sample_id] = {
            "condition": condition,
            "replicate": replicate
        }

print("Sample count:", len(samples))

condition_counts = {}

for sample_id, sample_info in samples.items():
    condition = sample_info["condition"]
    replicate = sample_info["replicate"]

    print(
        f"Sample: {sample_id}, "
        f"Condition: {condition}, "
        f"Replicate: {replicate}"
    )

    if condition not in condition_counts:
        condition_counts[condition] = 0

    condition_counts[condition] = condition_counts[condition] + 1

print("Condition counts:")

for condition, count in condition_counts.items():
    print(condition, count)
    