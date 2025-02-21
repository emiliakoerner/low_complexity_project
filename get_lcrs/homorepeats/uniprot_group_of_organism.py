import pandas as pd
import os
os.chdir()
# Load your data (assuming you have it in a CSV)
df = pd.read_csv('uniprot_data.csv')

# Define a function to classify based on the taxonomy
def categorize_organism(lineage):
    lineage = lineage.lower()  # Convert to lowercase for easier matching

    if "bacteria" in lineage:
        return "Bacteria"
    elif "archaea" in lineage:
        return "Archaea"
    elif "fungi" in lineage:
        return "Fungi"
    elif "vertebrata" in lineage or "chordata" in lineage:
        return "Vertebrates"
    elif "plantae" in lineage or "viridiplantae" in lineage:
        return "Plants"
    elif "eukaryota" in lineage:
        return "Protists"  # For this, you may need more advanced rules
    else:
        return "Invertebrates"  # Default case for anything that doesn’t fit above

# Apply the function to each row in the dataframe
df['Group_of_Organism'] = df['Taxonomic lineage'].apply(categorize_organism)

# Save the updated dataframe as a TSV file
df.to_csv('categorized_uniprot_data.tsv', sep='\t', index=False)

print("Data categorized and saved.")
