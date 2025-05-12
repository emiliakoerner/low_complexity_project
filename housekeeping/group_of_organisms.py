import pandas as pd
import sys
import os
sys.path.append(os.path.abspath('lib'))
from goO_constants import *
from constants import *

def categorize_organism(lineage):
    if not isinstance(lineage, str):
        return "Unknown"  # Or "Unclassified" or another default value for invalid rows

    lineage = lineage.split(", ")  # Convert string to list for easier matching

    if any(taxon in BACTERIA for taxon in lineage):
        return "Bacteria"
    elif any(taxon in VIRUSES for taxon in lineage):
        return "Viruses"
    elif any(taxon in ARCHAEA for taxon in lineage):
        return "Archaea"
    elif any(taxon in FUNGI for taxon in lineage):
        return "Fungi"
    elif any(taxon in PLANTS for taxon in lineage):
        return "Plants"

    elif any(taxon in INVERTEBRATES for taxon in lineage):
        if any(taxon in VERTEBRATES for taxon in lineage):
            return "Vertebrates"
        else:
            return "Invertebrates"

    else:
        return "Protists"

def find_file_path(proteome_id, tax_id):
    tax_id = str(tax_id)
    for folder in TAXON_CATEGORIES:
        file_path = f"{REF_DIR}/{folder}/{proteome_id}/{proteome_id}_{tax_id}.fasta.gz"
        print(file_path)
        if os.path.exists(file_path):  # Check if the file actually exists
            return file_path, folder  # Return path & superregnum
    return None, None

# Example usage with your UniProt data
df = pd.read_csv("D:/Emilia/proteomes_all_2025_02_17.tsv/proteomes_all_2025_02_17.tsv", sep="\t")
# Apply the function to the lineage column
df["group_of_organism"] = df["Taxonomic lineage"].apply(categorize_organism)
# Locate file paths and superregna dynamically
df[["File_Path", "Superregnum"]] = df.apply(lambda row: pd.Series(find_file_path(row["Proteome Id"], row["Organism Id"])), axis=1)
# Remove root path from the File_Path column
df["File_Path"] = df["File_Path"].str.replace(f"{REF_DIR}/", "", regex=False)

# **Filter out rows where File_Path is None (i.e., the file wasn't found)**
df = df.dropna(subset=["File_Path"])
# Save the output
df.to_csv("output.tsv", sep="\t", index=False)
