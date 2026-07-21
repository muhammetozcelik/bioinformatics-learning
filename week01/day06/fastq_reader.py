import gzip
import math
import sys

def open_fastq(fastq_path):
    if fastq_path.endswith(".gz"):
        return gzip.open(fastq_path, "rt")

    return open(fastq_path, "r")


def calculate_quality_stats(quality):
    total_error_probability = 0
    q30_count = 0

    for character in quality:
        phred_score = ord(character) - 33
        error_probability = 10 ** (-phred_score / 10)

        total_error_probability = (
            total_error_probability + error_probability
        )

        if phred_score >= 30:
            q30_count = q30_count + 1

    average_error_probability = (
        total_error_probability / len(quality)
    )

    average_quality = (
        -10 * math.log10(average_error_probability)
    )

    q30_percent = q30_count / len(quality) * 100

    return average_quality, q30_percent


if len(sys.argv) != 2:
    print("Usage: python fastq_reader.py <input.fastq>")
    sys.exit(1)


fastq_path = sys.argv[1]
read_count = 0

with open_fastq(fastq_path) as fastq_file:
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
        average_quality, q30_percent = calculate_quality_stats(
            quality
        )

        print("Read name:", read_name)
        print("Sequence:", sequence)
        print("Length:", len(sequence))
        print(f"Average quality: {average_quality:.2f}")
        print(f"Q30 bases: {q30_percent:.2f}%")

print("Total reads:", read_count)