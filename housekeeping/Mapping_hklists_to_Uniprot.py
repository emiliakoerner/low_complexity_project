# Mapping housekeeping lists from different sources to UniProt using underlying data from UniProt ID mapping tool
# Import python modules
import os
import sys
sys.path.append(os.path.abspath('../../lib'))
from constants import *
from load_organisms import organisms


def remove_suffix(uniprot_id):
    return re.sub(r"\.\d+$", "", uniprot_id) # Arabidopsis gene names have suffixes like AT12345.1
# Function to map Housekeeping gene lists to Uniprot using the
# underlying data files of the Uniprot Mapping tool.
def Housekeeping_mapping_uniprot(hk_file, mapping_file, hk_list):
    with open(mapping_file, 'r') as mapping:
        mapping_lines = mapping.readlines()     # Mapping file is read into python storage
    with open(hk_file, 'r') as hk_file, open(hk_list, 'w') as output:
        for line in hk_file:
            listid = line.strip().split("\t")[0]    # Hk genes are stored and iterated through
            if up_id == "UP000006548":
                listid = listid.split(".")[0]       # in case there is a suffix like ".1"
            for line2 in mapping_lines:
                columns = line2.strip().split("\t")
                mapid = columns[2]     # species-specific IDs are always in the third column of the mapping file
                #print(f"Checking if {listid} == {mapid}")  # Debug print
                if listid == mapid:     # If a matching entry in the mapping file is found,
                    uniprot_id = columns[0]     # The Uniprot ID is stored and written into an output file with both IDs
                    output.write(f"{listid}\t{uniprot_id}\n")
                    break

# Define dynamic file paths for each organism
file_paths = {}
for up_id in organisms:
    file_paths[up_id] = {
        # Data
        'UNMAPPED_HK_LIST_FILE': os.path.join(MAINTABLES_DIR, f"hk_unmapped/{up_id}_hk_unmapped.txt"),
        'HK_LIST_FILE': os.path.join(HK_LISTS_DIR, f"{up_id}_hk.txt"),
        # Results
        'MAPPED_HK_POLYX_FILE': os.path.join(OUTPUT_DIR, f"proteomes_hrs_hk/{up_id}_hrs_hk.tsv")
    }
    hk_file = file_paths[up_id]['UNMAPPED_HK_LIST_FILE']
    mapping_file = globals().get(f"{up_id}_mapping")
    hk_list = file_paths[up_id]['HK_LIST_FILE']

    print(f"Processing {hk_file}... with mapping file {mapping_file}, creating {hk_list}")  # Print status update
    if mapping_file is None:
        print(f"ERROR: Mapping file for {up_id} is None! Check variable name.")
        continue  # Skip to next organism
    if not os.path.exists(hk_file):
        print(f"ERROR: hk_file not found -> {hk_file}")
        continue
    if not os.path.exists(mapping_file):
        print(f"ERROR: mapping_file not found -> {mapping_file}")
        continue

    Housekeeping_mapping_uniprot(hk_file, mapping_file, hk_list)

