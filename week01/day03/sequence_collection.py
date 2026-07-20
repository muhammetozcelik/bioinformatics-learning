sequences = {
    "sample_1": "ATGCTAGCTAGCTACGATCG",
    "sample_2": "ATGCCCGGTTAA",
    "sample_3": "GGCCAATT"
}

total_length = 0
longest_name = ""
longest_length = 0

for name, sequence in sequences.items():
    sequence_length = len(sequence)
    total_length = total_length + sequence_length

    if sequence_length > longest_length:
        longest_name = name
        longest_length = sequence_length

average_length = total_length / len(sequences)

print("Sequence count:", len(sequences))
print("Total length:", total_length)
print(f"Average length: {average_length:.2f}")
print("Longest sequence:", longest_name)
print("Longest length:", longest_length)
