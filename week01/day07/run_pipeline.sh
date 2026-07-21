#!/usr/bin/env bash

set -euo pipefail

mkdir -p week01/day07/results

echo "1/3 Validating metadata..."
python week01/day04/validate_metadata.py \
    week01/day03/data/experiment_metadata.csv

echo "2/3 Creating FASTA summary..."
python week01/day02/fasta_summary.py \
    week01/day01/data/example.fasta \
    week01/day07/results/fasta_summary.tsv

echo "3/3 Creating FASTQ quality report..."
python week01/day06/fastq_reader.py \
    week01/day06/data/example.fastq \
    > week01/day07/results/fastq_report.txt

echo "Pipeline completed successfully."
