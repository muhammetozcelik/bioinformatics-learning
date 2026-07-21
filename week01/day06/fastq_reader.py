import sys


def calculate_quality_stats(quality):
    quality_scores = []

    for character in quality:
        phred_score = ord(character) - 33
        quality_scores.append(phred_score)

    average_quality = sum(quality_scores) / len(quality_scores)

    q30_count = 0

    for phred_score in quality_scores:
        if phred_score >= 30:
            q30_count = q30_count + 1

    q30_percent = q30_count / len(quality_scores) * 100

    return average_quality, q30_percent


fastq_path = "week01/day06/data/example.fastq"
read_count = 0

with open(fastq_path, "r") as fastq_file:
    while True:
        header = fastq_file.readline().strip()

        if header == "":
            break

        sequence = fastq_file.readline().strip()
        separator = fastq_file.readline().strip()
        quality = fastq_file.readline().strip()

        read_count = read_count + 1

        if not header.startswith("@"):
            print("Error: invalid FASTQ header:", header)
            sys.exit(1)

        if separator != "+":
            print("Error: invalid FASTQ separator:", separator)
            sys.exit(1)

        if len(sequence) != len(quality):
            print("Error: sequence and quality lengths differ")
            sys.exit(1)

        read_name = header[1:]
        average_quality, q30_percent = calculate_quality_stats(quality)

        print("Read name:", read_name)
        print("Sequence:", sequence)
        print("Length:", len(sequence))
        print(f"Average quality: {average_quality:.2f}")
        print(f"Q30 bases: {q30_percent:.2f}%")

print("Total reads:", read_count)
