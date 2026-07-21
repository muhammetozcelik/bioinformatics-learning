# Week 1 analysis pipeline

This pipeline combines the metadata, FASTA and FASTQ tools developed during week 1.

## Run

From the repository root, run `./week01/day07/run_pipeline.sh`.

## Steps

1. Validate experiment metadata.
2. Generate sequence length and GC summaries from FASTA.
3. Generate read length, average quality and Q30 reports from FASTQ.

## Outputs

- `results/fasta_summary.tsv`
- `results/fastq_report.txt`

The pipeline stops immediately if any step fails.