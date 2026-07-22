#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 3 ]]; then
    echo "Usage: $0 <R1.fastq[.gz]> <R2.fastq[.gz]> <output_directory>"
    exit 1
fi

read1="$1"
read2="$2"
output_dir="$3"
threads="${THREADS:-2}"

for input_file in "$read1" "$read2"; do
    if [[ ! -f "$input_file" ]]; then
        echo "Error: input file not found: $input_file"
        exit 1
    fi
done

for tool in seqkit fastqc fastp multiqc; do
    if ! command -v "$tool" > /dev/null 2>&1; then
        echo "Error: required tool not found: $tool"
        exit 1
    fi
done

read1_name="$(basename "$read1")"
sample_name="${read1_name%%_R1*}"

if [[ "$sample_name" == "$read1_name" ]]; then
    sample_name="${read1_name%%.*}"
fi

raw_fastqc_dir="$output_dir/raw_fastqc"
trimmed_dir="$output_dir/trimmed"
trimmed_fastqc_dir="$output_dir/trimmed_fastqc"
report_dir="$output_dir/reports"
multiqc_dir="$output_dir/multiqc"

trimmed_read1="$trimmed_dir/${sample_name}_trimmed_R1.fastq.gz"
trimmed_read2="$trimmed_dir/${sample_name}_trimmed_R2.fastq.gz"

mkdir -p \
    "$raw_fastqc_dir" \
    "$trimmed_dir" \
    "$trimmed_fastqc_dir" \
    "$report_dir" \
    "$multiqc_dir"

echo "1/6 Calculating raw read statistics..."

seqkit stats --all --tabular \
    "$read1" \
    "$read2" \
    > "$report_dir/raw_seqkit_stats.tsv"

echo "2/6 Running FastQC on raw reads..."

fastqc \
    --threads "$threads" \
    --outdir "$raw_fastqc_dir" \
    "$read1" \
    "$read2"

echo "3/6 Trimming paired reads with fastp..."

fastp \
    --in1 "$read1" \
    --in2 "$read2" \
    --out1 "$trimmed_read1" \
    --out2 "$trimmed_read2" \
    --detect_adapter_for_pe \
    --cut_tail \
    --cut_window_size 4 \
    --cut_mean_quality 20 \
    --length_required 20 \
    --thread "$threads" \
    --html "$report_dir/fastp_report.html" \
    --json "$report_dir/fastp_report.json"

echo "4/6 Calculating trimmed read statistics..."

seqkit stats --all --tabular \
    "$trimmed_read1" \
    "$trimmed_read2" \
    > "$report_dir/trimmed_seqkit_stats.tsv"

echo "5/6 Running FastQC on trimmed reads..."

fastqc \
    --threads "$threads" \
    --outdir "$trimmed_fastqc_dir" \
    "$trimmed_read1" \
    "$trimmed_read2"

echo "6/6 Creating combined MultiQC report..."

multiqc \
    "$raw_fastqc_dir" \
    "$trimmed_fastqc_dir" \
    "$report_dir" \
    --outdir "$multiqc_dir" \
    --filename qc_report.html \
    --force

echo "QC pipeline completed successfully."
echo "Trimmed R1: $trimmed_read1"
echo "Trimmed R2: $trimmed_read2"
echo "MultiQC report: $multiqc_dir/qc_report.html"
