def read_fasta(fasta_path):
    sequences = {}

    current_name = ""
    current_sequence = ""

    with open(fasta_path, "r") as fasta_file:
        for line in fasta_file:
            clean_line = line.strip()

            if clean_line == "":
                continue

            if clean_line.startswith(">"):
                if current_name != "":
                    sequences[current_name] = current_sequence

                current_name = clean_line[1:]
                current_sequence = ""
            else:
                current_sequence = current_sequence + clean_line.upper()

    if current_name != "":
        sequences[current_name] = current_sequence

    return sequences


fasta_path = "week01/day01/data/example.fasta"
records = read_fasta(fasta_path)

print("Sequence count:", len(records))

for name, sequence in records.items():
    print("Sequence name:", name)
    print("DNA sequence:", sequence)
    print("Length:", len(sequence))
total_length = 0

for sequence in records.values():
    total_length = total_length + len(sequence)

average_length = total_length / len(records)

print("Total length:", total_length)
print(f"Average length: {average_length:.2f}")
 