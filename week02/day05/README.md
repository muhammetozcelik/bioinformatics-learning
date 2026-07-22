# Paired-End RNA-seq Quality Control Pipeline

This directory contains a reproducible quality-control pipeline for
paired-end RNA-seq FASTQ files.

## Workflow

The pipeline performs the following steps:

1. Calculates raw FASTQ statistics with SeqKit.
2. Runs FastQC on the raw paired reads.
3. Performs paired-end adapter and quality trimming with fastp.
4. Calculates statistics for the trimmed reads.
5. Runs FastQC on the trimmed reads.
6. Combines all reports with MultiQC.

## Environment

Activate the reproducible Micromamba environment:

```bash
micromamba activate bioinfo-week02
```

The environment is defined in:

```text
week02/environment.yml
```

## Usage

Run the pipeline from the repository root:

```bash
./week02/day05/run_qc_pipeline.sh \
  week02/day02/data/GSM461178_R1.fastq \
  week02/day02/data/GSM461178_R2.fastq \
  week02/day05/output
```

The script accepts three arguments:

```text
run_qc_pipeline.sh <R1.fastq[.gz]> <R2.fastq[.gz]> <output_directory>
```

## Trimming strategy

fastp is configured with:

- Paired-end adapter detection
- 3-prime sliding-window quality trimming
- Window size of 4 bases
- Mean quality threshold of Q20
- Minimum retained read length of 20 bases
- Two processing threads by default

The number of threads can be changed with an environment variable:

```bash
THREADS=4 ./week02/day05/run_qc_pipeline.sh R1.fastq R2.fastq output
```

## Dataset results

For the GSM461178 paired-end RNA-seq subset:

- Input read pairs: 100,000
- Retained read pairs: 98,376
- Retained pairs: 98.38%
- R1 Q30: 91.29% to 92.40%
- R2 Q30: 82.28% to 85.41%
- R2 FastQC per-base quality: WARN to PASS
- Reads with adapters trimmed: 756
- fastp duplication estimate: 0.899%

## Reproducibility verification

The manually generated and pipeline-generated trimmed FASTQ contents
produced identical MD5 hashes after decompression:

```text
R1: 16c2eebb847a314b4f51aa41ded26a49
R2: 42a662b257a8f4cb8c4563610415ad33
```

## Output directories

```text
output/
├── raw_fastqc/
├── reports/
├── trimmed/
├── trimmed_fastqc/
└── multiqc/
```

Generated FASTQ files and reports are excluded from Git. The pipeline,
environment definition, parameters, and interpretation notes are
version controlled.

## Tools

- [SeqKit](https://bioinf.shenwei.me/seqkit/)
- [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)
- [fastp](https://github.com/OpenGene/fastp)
- [MultiQC](https://docs.seqera.io/multiqc)
