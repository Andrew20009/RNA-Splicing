CODON_TABLE = { #Codon table to transform mRNA into the amino acids and make a polypeptide chain
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}


def read_dna_from_txt(file_path: str) -> dict[str, str]: # Reads FASTA-formatted DNA sequences into id: sequence
    sequences: dict[str, str] = {} # Create an empty dictionary for pairs
    current_id = "" # Create empty variable for the current ID
    with open(file_path) as f: # Open the file for reading
        for line in f:
            cleaned = line.strip() # Remove leading or trailing whitespace
            if not cleaned: # Skip blank lines
                continue
            if cleaned.startswith(">"):  # Check if this line is a FASTA header
                current_id = cleaned[1:] # Use the text after '>' as the sequence id
                sequences[current_id] = "" # Start a fresh empty sequence for this id
            else:
                sequences[current_id] += cleaned.upper() # Uppercase only the sequence bases
    return sequences


def splice_introns(dna: str, introns: list[str]) -> str: # Removes every intron occurrence from the DNA string
    for intron in introns: # Go through each intron sequence one by one
        dna = dna.replace(intron, "") # Cut every occurrence of this intron out of the DNA
    return dna # Return the DNA string with all introns removed


def transcribe_to_rna(dna: str) -> str: # Converts DNA to RNA by swapping T for U
    return dna.replace("T", "U") # Replace every thymine nitrogenous base with uracil nitrogenous base


def translate_rna(rna: str) -> str: # Translates codon-by-codon until a stop codon is hit
    protein = [] # Create an empty list to collect amino acids
    for i in range(0, len(rna) - 2, 3): # Step through the RNA three bases at a time
        codon = rna[i:i + 3] # Slice out the current codon
        amino_acid = CODON_TABLE[codon] # Look up the amino acid for this codon
        if amino_acid == "*": # Check if this codon is a stop codon
            break # Stop translating once a stop codon is reached
        protein.append(amino_acid) # Add the translated amino acid to the chain
    return "".join(protein) # Join all amino acids into the final polypeptide string


def main() -> None: # Entry point that runs the full splicing to protein
    sequences = read_dna_from_txt("rosalind_splc.txt") # Load the main DNA string and all intron sequences
    ids = list(sequences) # Get the FASTA ids in the order they were read
    dna, introns = sequences[ids[0]], [sequences[i] for i in ids[1:]] # First id is the DNA, the rest are introns

    exon_dna = splice_introns(dna, introns) # Remove the introns to leave only exon DNA
    rna = transcribe_to_rna(exon_dna) # Transcribe the exon DNA into RNA
    protein = translate_rna(rna) # Translate the RNA into a polypeptide chain

    print(protein) # Print the resulting protein string


if __name__ == "__main__": # Only run main() when this file is executed directly
    main()
