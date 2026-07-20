import sys


def write_sequence_summary(summary_file, name, sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percent = gc_count / len(sequence) * 100

    summary_file.write(
        f"{name}\t{len(sequence)}\t{gc_percent:.2f}\n"
    )


def create_summary(input_path, output_path):
    sequence_name = ""
    sequence = ""

    with open(input_path, "r") as fasta_file, open(output_path, "w") as summary_file:
        summary_file.write("sequence_name\tlength\tgc_percent\n")

        for line in fasta_file:
            clean_line = line.strip()

            if clean_line == "":
                continue

            if clean_line.startswith(">"):
                if sequence_name != "":
                    write_sequence_summary(
                        summary_file, sequence_name, sequence
                    )

                sequence_name = clean_line[1:]
                sequence = ""
            else:
                sequence = sequence + clean_line.upper()

        if sequence_name != "":
            write_sequence_summary(
                summary_file, sequence_name, sequence
            )


if len(sys.argv) != 3:
    print("Usage: python fasta_summary.py <input.fasta> <output.tsv>")
    sys.exit(1)


input_path = sys.argv[1]
output_path = sys.argv[2]

try:
    create_summary(input_path, output_path)
except FileNotFoundError as error:
    print("Error: file or directory not found:", error.filename)
    sys.exit(1)

print("Summary written to:", output_path)
