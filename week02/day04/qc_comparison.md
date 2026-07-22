# Raw and Trimmed Read Quality Comparison

## Dataset

Paired-end RNA-seq reads:

- GSM461178_R1
- GSM461178_R2
- 100,000 input read pairs
- Original read length: 37 bp

## Trimming parameters

The paired reads were processed with fastp using:

- Paired-end adapter detection
- 3-prime sliding-window quality trimming
- Window size: 4
- Mean quality threshold: Q20
- Minimum retained length: 20 bp
- Threads: 2

## Results

| Metric | Raw R1 | Trimmed R1 | Raw R2 | Trimmed R2 |
|---|---:|---:|---:|---:|
| Read count | 100,000 | 98,376 | 100,000 | 98,376 |
| Average length | 37.0 bp | 36.7 bp | 37.0 bp | 35.8 bp |
| Q30 bases | 91.29% | 92.40% | 82.28% | 85.41% |
| FastQC per-base quality | PASS | PASS | WARN | PASS |

A total of 98.38% of the input read pairs passed filtering. Adapter
trimming affected only 0.4% of reads, indicating that adapter
contamination was not a major issue.

## Interpretation

The raw R2 reads showed stronger quality degradation toward the
3-prime end than R1. Quality-based tail trimming improved the R2 Q30
percentage and changed its FastQC per-base quality result from WARN to
PASS while retaining most read pairs.

The sequence length distribution warning after trimming is expected
because quality trimming creates reads of different lengths.

Per-base sequence content and GC-content warnings remained after
trimming. These warnings may reflect RNA-seq library preparation or
priming bias and are not, by themselves, evidence of adapter
contamination. Additional trimming was therefore not performed merely
to force all FastQC modules to pass.

## Decision

The trimmed paired-end reads are suitable for the next downstream
analysis step. Pair synchronization was preserved, and the quality
improvement was achieved with limited data loss.