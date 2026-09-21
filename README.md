# RNA Splicing

## OVERVIEW
This program removes introns from a DNA string, splices the remaining exons together, transcribes the result into RNA, and translates it into a protein string using the codon table.
It is a solution to the **"RNA Splicing"** Rosalind problem **(ID: SPLC)**. The tool is simple, efficient, and ideal for practicing string processing, file handling, and codon translation in Python.

---

## FEATURES
- Reads multiple FASTA-formatted DNA sequences from a file (`rosalind_splc.txt`), where the first record is the DNA string and every following record is an intron
- Removes every occurrence of each intron from the DNA string
- Transcribes the spliced exon DNA into RNA
- Translates the RNA codon-by-codon into amino acids using the standard RNA codon table, stopping at any stop codon
- Clean, well-commented code with proper functions and type hints

---

## ⚠️ IMPORTANT NOTE
> <u>**!!!Please put the input FASTA file with name rosalind_splc.txt in the same folder as the code, otherwise you will receive an Error File Not Found!!!**</u>

---

## EXAMPLE
**Input** (rosalind_splc.txt):
```
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
```
**Output:**
```
MVYIADKQHVASREAYGHMFKVCA
```

---

## HOW IT WORKS
1. The program reads the FASTA file and builds a dictionary mapping each sequence ID to its full sequence
2. The first sequence is treated as the DNA string, and every remaining sequence is treated as an intron
3. Each intron is removed from the DNA string wherever it occurs, leaving only the spliced exon DNA
4. The exon DNA is transcribed into RNA by replacing every `T` with `U`
5. The RNA is translated 3 nucleotides, which equals one codon, at a time into amino acids using the RNA codon table, stopping as soon as a stop codon is reached
6. Finally, it prints the resulting protein string

---

## TECHNOLOGIES USED
- **Python**
- **TXT File**
