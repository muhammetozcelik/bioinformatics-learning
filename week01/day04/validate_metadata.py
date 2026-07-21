import csv
import sys


if len(sys.argv) != 2:
    print("Usage: python validate_metadata.py <metadata.csv>")
    sys.exit(1)


metadata_path = sys.argv[1]

required_columns = {
    "sample_id",
    "condition",
    "replicate"
}

sample_ids = set()
errors = []
row_count = 0

try:
    with open(metadata_path, "r") as metadata_file:
        reader = csv.DictReader(metadata_file)

        actual_columns = set(reader.fieldnames or [])
        missing_columns = required_columns - actual_columns

        if len(missing_columns) > 0:
            print("Metadata invalid: required columns are missing.")

            for column in sorted(missing_columns):
                print("Missing column:", column)

            sys.exit(1)

        for line_number, row in enumerate(reader, start=2):
            row_count = row_count + 1

            sample_id = row["sample_id"].strip()
            condition = row["condition"].strip()
            replicate_text = row["replicate"].strip()

            if sample_id == "":
                errors.append(
                    f"Line {line_number}: sample_id cannot be empty"
                )
            elif sample_id in sample_ids:
                errors.append(
                    f"Line {line_number}: duplicate sample_id: {sample_id}"
                )
            else:
                sample_ids.add(sample_id)

            if condition == "":
                errors.append(
                    f"Line {line_number}: condition cannot be empty"
                )

            try:
                replicate = int(replicate_text)

                if replicate < 1:
                    errors.append(
                        f"Line {line_number}: replicate must be positive"
                    )

            except ValueError:
                errors.append(
                    f"Line {line_number}: replicate must be an integer: "
                    f"{replicate_text}"
                )

except FileNotFoundError:
    print("Error: metadata file not found:", metadata_path)
    sys.exit(1)


if len(errors) > 0:
    print("Metadata invalid:")

    for error in errors:
        print("-", error)

    sys.exit(1)


print("Metadata valid.")
print("Sample count:", row_count)
