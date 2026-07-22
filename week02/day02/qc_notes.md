# Raw paired-end RNA-seq QC

## Dataset

- Sample: GSM461178
- Organism: Drosophila melanogaster
- Layout: paired-end
- Read length: 37 bp
- Source: Zenodo record 61771

## FastQC findings

### R1

- Per-base quality passed.
- Mean quality decreases slightly near the read end.
- No adapter contamination was detected.

### R2

- Per-base quality produced a warning.
- Quality variability increases after approximately base 20.
- The strongest quality loss occurs around bases 32-37.
- No adapter contamination was detected.

### Sequence-content bias

Both reads show strong base-composition bias in approximately the first
10-12 positions. The pattern stabilizes afterwards and may reflect
RNA-seq library preparation or priming bias.

## Decision

Use paired-end, quality-based tail trimming. Preserve read pairing and
order. Do not remove the first bases solely to make the FastQC module
pass.