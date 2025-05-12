import os
import sys
import re

sys.path.append(os.path.abspath('../lib'))
from constants import *
from load_organisms import organisms

# Remove suffixes like ".1" for Arabidopsis
def remove_suffix(uniprot_id):
    return re.sub(r"\.\d+$", "", uniprot_id)

# For organisms with internal mapping file
def Housekeeping_mapping_uniprot(hk_file, mapping_file, hk_list):
    with open(mapping_file, 'r') as mapping:
        mapping_lines = mapping.readlines()

    with open(hk_file, 'r') as hk_file, open(hk_list, 'w') as output:
        for line in hk_file:
            listid = line.strip().split("\t")[0]
            if up_id == "UP000006548":
                listid = listid.split(".")[0]
            for line2 in mapping_lines:
                columns = line2.strip().split("\t")
                if len(columns) < 3:
                    continue
                mapid = columns[2]
                if listid == mapid:
                    uniprot_id = columns[0]
                    output.write(f"{listid}\t{uniprot_id}\n")
                    break

# For organisms mapped via UniProt web tool
def normalize_uniprot_mapping(uniprot_mapping_file, output_file):
    with open(uniprot_mapping_file, 'r') as infile, open(output_file, 'w') as outfile:
        next(infile)  # Skip header
        for line in infile:
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                original_id = parts[0]
                uniprot_id = parts[1]
                outfile.write(f"{original_id}\t{uniprot_id}\n")

# === MAIN PROCESS ===
for up_id in organisms:
    hk_list = os.path.join(HK_LISTS_DIR, f"{up_id}_hk.txt")

    # Path if needs internal mapping
    hk_file_mapped = os.path.join(MAINTABLES_DIR, f"hk_unmapped/{up_id}_hk_unmapped.txt")
    mapping_file = globals().get(f"{up_id}_mapping")

    # Path if already mapped via UniProt tool
    hk_file_uniprot = os.path.join(MAINTABLES_DIR, f"uniprot_id_mapping_tool/{up_id}.tsv")

    if os.path.exists(hk_file_mapped) and mapping_file and os.path.exists(mapping_file):
        print(f"[{up_id}] Using internal mapping: {hk_file_mapped} + {mapping_file} → {hk_list}")
        Housekeeping_mapping_uniprot(hk_file_mapped, mapping_file, hk_list)
    elif os.path.exists(hk_file_uniprot):
        print(f"[{up_id}] Using UniProt tool file: {hk_file_uniprot} → {hk_list}")
        normalize_uniprot_mapping(hk_file_uniprot, hk_list)
    else:
        print(f"[{up_id}] ERROR: No valid mapping or UniProt file found.")
