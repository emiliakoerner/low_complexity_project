import pandas as pd
import sys
import os
sys.path.append(os.path.abspath('lib'))
from goO_constants import *
from constants import *

# Function to categorize host organisms (for viruses)
def categorize_host(lineage):
    if not isinstance(lineage, str) or pd.isna(lineage):
        return "Unknown"

    lineage = lineage.split("; ")

    if any(taxon in BACTERIA for taxon in lineage):
        return "Bacteria"
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

# Function to categorize non-viruses by their own type
def categorize_non_virus(group_of_organism):
    if group_of_organism in BACTERIA:
        return "Bacteria"
    elif group_of_organism in ARCHAEA:
        return "Archaea"
    elif group_of_organism in FUNGI:
        return "Fungi"
    elif group_of_organism in PLANTS:
        return "Plants"
    elif group_of_organism in VERTEBRATES:
        return "Vertebrates"
    elif group_of_organism in INVERTEBRATES:
        return "Invertebrates"
    else:
        return "Protists"

# Function to determine superregnum
def determine_superregnum(group_of_organism, host_group):
    if group_of_organism in VIRUSES:
        if host_group in ["Bacteria", "Archaea"]:
            return "Phage"
        elif host_group in ["Fungi", "Plants", "Vertebrates", "Invertebrates", "Protists"]:
            return "Virus"
        else: return "Unknown"
    else:
        return "Prokaryotes" if group_of_organism in ["Bacteria", "Archaea"] else "Eukaryotes"

# Load main dataset
df = pd.read_csv("D:/Emilia/low_complexity_project/main_tables/proteomes_uniprot_2024_06.tsv", sep="\t")

# Load virus-host information
df_host_info = pd.read_csv("D:/Emilia/virushostdb.tsv", sep="\t")
df_host_info = df_host_info[['virus tax id', 'host lineage']]

# Ensure correct column types before merging
df['tax_id'] = df['tax_id'].astype(str)
df_host_info['virus tax id'] = df_host_info['virus tax id'].astype(str)

# Merge virus data with host info
df_host_info = df_host_info.drop_duplicates(subset=['virus tax id'])
df = df.merge(df_host_info, left_on='tax_id', right_on='virus tax id', how='left')

# Apply host classification only for viruses
df["host_group"] = df["host lineage"].apply(categorize_host)

# Apply self-classification for non-viruses
df.loc[~df["group_of_organism"].isin(VIRUSES), "host_group"] = df["group_of_organism"].apply(categorize_non_virus)

# Determine superregnum
df["supergroup"] = df.apply(lambda row: determine_superregnum(row["group_of_organism"], row["host_group"]), axis=1)

# Remove unwanted columns ('virus tax id' and 'host lineage')
df.drop(columns=['virus tax id', 'host lineage'], inplace=True)
print("Final dataset rows:", df.shape[0])

# Convert host tax ids to a set for fast lookup
host_tax_ids = set(df_host_info["host tax id"].astype(str))

# Update supergroup for hosts
df.loc[df["tax_id"].isin(host_tax_ids) & (df["supergroup"] == "Eukaryotes"), "supergroup"] = "Eukaryotic host"
df.loc[df["tax_id"].isin(host_tax_ids) & (df["supergroup"] == "Prokaryotes"), "supergroup"] = "Prokaryotic host"

# Print counts to check changes
print(df["supergroup"].value_counts())

# Save output
df.to_csv("output_with_host_groups_and_supergroup.tsv", sep="\t", index=False)