import os
import re
from collections import defaultdict
import sys
sys.path.append(os.path.abspath('../../lib'))
from constants import *

def Genelength(biomartfile):  # Read biomart file into a dictionary
    global biomartdict
    biomartdict = defaultdict(lambda: {"gene_id": "", "swiss_id": "", "trembl_id": "", "gene_length": 0})
    with open(biomartfile) as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split("\t")  # store each column in a variable
            gene_id = parts[0]
            swiss_id = parts[2]
            trembl_id = parts[3]
            start = int(parts[4])
            end = int(parts[5])
            length = end - start  # calculate gene length
            # some proteins have swiss id, some trembl id, some both. Use swiss id as a key if there is one and the same
            # with trembl ID to make sure both IDs are in the dictionary with no errors either
            if swiss_id:
                biomartdict[swiss_id] = {"gene_id": gene_id, "swiss_id": swiss_id, "trembl_id": trembl_id,
                                         "gene_length": length}
            if trembl_id:
                biomartdict[trembl_id] = {"gene_id": gene_id, "swiss_id": swiss_id, "trembl_id": trembl_id,
                                          "gene_length": length}


def Create_genelength_doc(inputfile, outputfile):
    with open(inputfile, 'r') as input, open(outputfile, 'w') as output:
        output.write(f"Genename\tUniProtID\tLength\tHk\tgenelength\n")  # Header
        next(input)  # Skip header when reading input file
        for line in input:  # Go through each line of the file
            parts = line.strip("\n").split("\t")  # For each line, save each column in a variable
            gene_name = parts[0]
            uniprot_id = parts[1]
            length = parts[2]
            housekeeping = parts[9]

            if uniprot_id in biomartdict:  # swiss id or trembl id
                genelength = biomartdict[uniprot_id]["gene_length"]
            else:
                genelength = "-"
            output.write(f"{gene_name}\t{uniprot_id}\t{length}\t{housekeeping}\t{genelength}\n")


def Process_genelength(proteomes_hrs_hk, biomart_dir, output_dir):
    for file in os.listdir(proteomes_hrs_hk):
        if file.endswith("UP000000625_hrs_hk.tsv") or file.endswith("UP000006548_hrs_hk.tsv"):
            continue
        elif file.endswith("_hrs_hk.tsv"):
            species = file.replace("_hrs_hk.tsv", "")
            biomart_file = f"{species}_biomart.txt"
            biomart_path = os.path.join(biomart_dir, biomart_file)
            input_path = os.path.join(proteomes_hrs_hk, file)
            output_path = os.path.join(output_dir, f"{species}_length.tsv")
            print("processing", species)

            Genelength(biomart_path)
            Create_genelength_doc(input_path, output_path)

proteomes_hrs_hk = f"{REP_BASE_DIR}/analysis/proteomes_hrs_hk"
biomart_dir = f"{REP_BASE_DIR}/analysis/biomart"
output_dir = f"{REP_BASE_DIR}/analysis/genelengthoutput"

Process_genelength(proteomes_hrs_hk, biomart_dir, output_dir)