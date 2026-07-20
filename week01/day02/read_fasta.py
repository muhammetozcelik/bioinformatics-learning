def print_sequence_info(name, sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    gc_percent = (g_count + c_count) / len(sequence) * 100

    print("Sequence name:", name)
    print("DNA sequence:", sequence)
    print("Length:", len(sequence))
    print(f"GC percentage: {gc_percent:.2f}%")
    print()


fasta_path = "week01/day01/data/example.fasta"

sequence_name = ""
sequence = ""

with open(fasta_path, "r") as fasta_file:
    for line in fasta_file:
        clean_line = line.strip()

        if clean_line == "":
            continue

        if clean_line.startswith(">"):
            if sequence_name != "":
                print_sequence_info(sequence_name, sequence)

            sequence_name = clean_line[1:]
            sequence = ""
        else:
            sequence = sequence + clean_line.upper()

if sequence_name != "":
    print_sequence_info(sequence_name, sequence)
    

