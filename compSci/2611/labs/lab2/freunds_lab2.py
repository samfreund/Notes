#!/usr/bin/env python3
"""
Gene Optimization Tool

This script provides functionality to optimize and deoptimize gene sequences
based on codon frequency tables. It reads FASTA files containing gene sequences
and applies codon optimization to improve or reduce expression levels.
"""

import csv
import os
from typing import Dict, List, Union


def optimize_gene(
    gene_id: str, fasta_file_path: str, codon_freq_table_file_path: str
) -> Union[str, int]:
    """
    Optimize a gene sequence by replacing codons with the most frequently used codons
    for each amino acid.

    Args:
        gene_id (str): The identifier of the gene to optimize
        fasta_file_path (str): Path to the FASTA file containing gene sequences
        codon_freq_table_file_path (str): Path to the CSV file containing codon frequencies

    Returns:
        str: The optimized gene sequence, or -1 if gene not found
    """
    fasta = parse_fasta(fasta_file_path)
    if gene_id not in fasta:
        return -1

    gene = fasta[gene_id]
    # Split gene sequence into codons (triplets)
    codons = [gene[i : i + 3] for i in range(0, len(gene), 3)]

    codon_freq = parse_freq_table(codon_freq_table_file_path)
    optimized_gene = ""

    for codon in codons:
        # Find the amino acid for the current codon
        amino_acid_found = False
        for amino_acid in codon_freq:
            if codon in codon_freq[amino_acid]:
                # Get the most frequent codon (last in sorted list)
                optimized_gene += codon_freq[amino_acid][-1]
                amino_acid_found = True
                break

        # Handle case where codon is not found in frequency table
        if not amino_acid_found:
            print(
                f"Warning: Codon '{codon}' not found in frequency table. Using original codon."
            )
            optimized_gene += codon

    # Write optimized sequence to file
    output_filename = f"{gene_id}_optimized.fasta"
    with open(output_filename, "w") as file:
        file.write(f">{gene_id}\n")
        file.write(optimized_gene + "\n")

    print(f"Optimized sequence written to {output_filename}")
    return optimized_gene


def deoptimize_gene(
    gene_id: str, fasta_file_path: str, codon_freq_table_file_path: str
) -> Union[str, int]:
    """
    Deoptimize a gene sequence by replacing codons with the least frequently used codons
    for each amino acid.

    Args:
        gene_id (str): The identifier of the gene to deoptimize
        fasta_file_path (str): Path to the FASTA file containing gene sequences
        codon_freq_table_file_path (str): Path to the CSV file containing codon frequencies

    Returns:
        str: The deoptimized gene sequence, or -1 if gene not found
    """
    fasta = parse_fasta(fasta_file_path)
    if gene_id not in fasta:
        return -1

    gene = fasta[gene_id]
    # Split gene sequence into codons (triplets)
    codons = [gene[i : i + 3] for i in range(0, len(gene), 3)]

    codon_freq = parse_freq_table(codon_freq_table_file_path)
    deoptimized_gene = ""

    for codon in codons:
        # Find the amino acid for the current codon
        amino_acid_found = False
        for amino_acid in codon_freq:
            if codon in codon_freq[amino_acid]:
                # Get the least frequent codon (first in sorted list)
                deoptimized_gene += codon_freq[amino_acid][0]
                amino_acid_found = True
                break

        # Handle case where codon is not found in frequency table
        if not amino_acid_found:
            print(
                f"Warning: Codon '{codon}' not found in frequency table. Using original codon."
            )
            deoptimized_gene += codon

    # Write deoptimized sequence to file
    output_filename = f"{gene_id}_deoptimized.fasta"
    with open(output_filename, "w") as file:
        file.write(f">{gene_id}\n")
        file.write(deoptimized_gene + "\n")

    print(f"Deoptimized sequence written to {output_filename}")
    return deoptimized_gene


def parse_freq_table(codon_freq_table_file_path: str) -> Dict[str, List[str]]:
    """
    Parse a codon frequency table from a CSV file.

    Expected CSV format:
    codon,amino_acid,frequency
    TTT,F,0.45
    TTC,F,0.55
    ...

    Args:
        codon_freq_table_file_path (str): Path to the CSV file containing codon frequencies

    Returns:
        Dict[str, List[str]]: Dictionary mapping amino acids to lists of codons
                             ordered from least frequent to most frequent
    """
    codon_freq = {}

    if not os.path.exists(codon_freq_table_file_path):
        raise FileNotFoundError(
            f"Codon frequency table file not found: {codon_freq_table_file_path}"
        )

    with open(codon_freq_table_file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)  # Skip header and check if file is empty
        if header is None:
            raise ValueError("Codon frequency table file is empty")

        for row_num, row in enumerate(
            reader, start=2
        ):  # Start at 2 because we skipped header
            if len(row) != 3:
                print(f"Warning: Skipping malformed row {row_num}: {row}")
                continue

            codon, amino_acid, freq_str = row
            try:
                freq = float(freq_str)
            except ValueError:
                print(
                    f"Warning: Invalid frequency value '{freq_str}' in row {row_num}. Skipping."
                )
                continue

            if amino_acid not in codon_freq:
                codon_freq[amino_acid] = {}
            codon_freq[amino_acid][freq] = codon

    # Convert frequency-codon mappings to sorted codon lists
    for amino_acid in codon_freq:
        # Sort by frequency and extract codons (least frequent first)
        codon_freq[amino_acid] = [
            codon for freq, codon in sorted(codon_freq[amino_acid].items())
        ]

    return codon_freq


def parse_fasta(fasta_file_path: str) -> Dict[str, str]:
    """
    Parse a FASTA file and return a dictionary of gene sequences.

    Args:
        fasta_file_path (str): Path to the FASTA file

    Returns:
        Dict[str, str]: Dictionary mapping gene IDs to their sequences

    Raises:
        FileNotFoundError: If the FASTA file doesn't exist
    """
    if not os.path.exists(fasta_file_path):
        raise FileNotFoundError(f"FASTA file not found: {fasta_file_path}")

    sequences = {}
    with open(fasta_file_path, "r") as file:
        gene_id = None
        sequence = []

        for line in file:
            line = line.strip()
            if line.startswith(">"):
                # Save previous sequence if it exists
                if gene_id:
                    sequences[gene_id] = "".join(sequence)
                # Start new sequence
                gene_id = line[1:]  # Remove '>'
                sequence = []
            else:
                # Add to current sequence (remove any whitespace)
                sequence.append(line.replace(" ", "").replace("\t", ""))

        # Don't forget the last sequence
        if gene_id:
            sequences[gene_id] = "".join(sequence)

    return sequences


def menu():
    """
    Interactive menu system for gene optimization operations.
    """
    print("Gene Optimization Tool")
    print("=" * 22)

    # Get file paths once at the beginning
    while True:
        fasta_path = input("Enter the path to the FASTA file: ").strip()
        if os.path.exists(fasta_path):
            break
        print(f"Error: File '{fasta_path}' not found. Please try again.")

    while True:
        codon_freq_path = input(
            "Enter the path to the codon frequency table file: "
        ).strip()
        if os.path.exists(codon_freq_path):
            break
        print(f"Error: File '{codon_freq_path}' not found. Please try again.")

    # Main menu loop
    while True:
        print("\nMenu:")
        print("1. Optimize a gene")
        print("2. Deoptimize a gene")
        print("3. List available genes")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            gene_id = input("Enter the gene ID to optimize: ").strip()
            try:
                result = optimize_gene(gene_id, fasta_path, codon_freq_path)
                if result == -1:
                    print(f"Gene '{gene_id}' not found in FASTA file.")
                else:
                    print(f"Gene '{gene_id}' successfully optimized.")
            except Exception as e:
                print(f"Error during optimization: {e}")

        elif choice == "2":
            gene_id = input("Enter the gene ID to deoptimize: ").strip()
            try:
                result = deoptimize_gene(gene_id, fasta_path, codon_freq_path)
                if result == -1:
                    print(f"Gene '{gene_id}' not found in FASTA file.")
                else:
                    print(f"Gene '{gene_id}' successfully deoptimized.")
            except Exception as e:
                print(f"Error during deoptimization: {e}")

        elif choice == "3":
            try:
                fasta_data = parse_fasta(fasta_path)
                print(f"\nAvailable genes ({len(fasta_data)}):")
                for gene_id in sorted(fasta_data.keys()):
                    seq_length = len(fasta_data[gene_id])
                    print(f"  {gene_id} (length: {seq_length} bp)")
            except Exception as e:
                print(f"Error reading FASTA file: {e}")

        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    menu()
