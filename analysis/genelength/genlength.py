import os
import re
from collections import defaultdict
import sys
sys.path.append(os.path.abspath('../../lib'))
from constants import *

def Genelength(biomartfile):  # Read biomart file into a dictionary
    global lengthdict
    lengthdict = defaultdict(lambda: {"gene_id": "", "swiss_id": "", "trembl_id": "", "gene_length": 0})
    with open(biomartfile) as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split("\t")  # store each column in a variable
            gene_id = parts[0]
            swiss_id = parts[2]
            trembl_id = parts[3]
            start = int(parts[4])
            end = int(parts[5])
            length = end - start + 1  # calculate gene length
            # some proteins have swiss id, some trembl id, some both. Use swiss id as a key if there is one and the same
            # with trembl ID to make sure both IDs are in the dictionary with no errors either
            if swiss_id:
                lengthdict[swiss_id] = {"gene_id": gene_id, "swiss_id": swiss_id, "trembl_id": trembl_id,
                                         "gene_length": length}
            if trembl_id:
                lengthdict[trembl_id] = {"gene_id": gene_id, "swiss_id": swiss_id, "trembl_id": trembl_id,
                                          "gene_length": length}

def Genelength_from_gtf(gtf_file, id_key="gene"):
    global lengthdict
    lengthdict = {}

    with open(gtf_file, 'r') as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.strip().split('\t')
            if len(parts) < 9 or parts[2] != "gene":
                continue

            start = int(parts[3])
            end = int(parts[4])
            length = end - start + 1

            attributes = parts[8]
            attr_dict = {}
            for attr in attributes.split(';'):
                attr = attr.strip()
                if not attr:
                    continue
                if ' ' in attr:
                    key, val = attr.split(' ', 1)
                    attr_dict[key] = val.strip('"')

            gene_id = attr_dict.get(id_key)
            if gene_id:
                lengthdict[gene_id] = {
                    "gene_id": gene_id,
                    "gene_length": length
                }

def Create_genelength_doc(inputfile, outputfile, match_by_gene_name=False, force_upper=False):
    with open(inputfile, 'r') as input, open(outputfile, 'w') as output:
        output.write(f"Genename\tUniProtID\tLength\tHk\tgenelength\n")  # Header
        next(input)  # Skip header when reading input file
        for line in input:
            parts = line.strip("\n").split("\t")
            gene_name = parts[0]
            uniprot_id = parts[1]
            length = parts[2]
            housekeeping = parts[9]

            lookup_id = gene_name if match_by_gene_name else uniprot_id
            if force_upper:
                lookup_id = lookup_id.upper()

            if lookup_id in lengthdict:
                genelength = lengthdict[lookup_id]["gene_length"]
            else:
                genelength = "-"

            output.write(f"{gene_name}\t{uniprot_id}\t{length}\t{housekeeping}\t{genelength}\n")


def Process_genelength(proteomes_hrs_hk, biomart_dir, output_dir):
    gtf_id_keys = {
        "UP000000625": "gene",       # E. coli
        "UP000006548": "gene_id"     # Arabidopsis
    }

    case_sensitive_lookup = {
        "UP000000625": True,    # E. coli → case-sensitive gene names
        "UP000006548": False    # Arabidopsis → lowercase ATG IDs → needs uppercase
    }

    for file in os.listdir(proteomes_hrs_hk):
        if file.endswith("_hrs_hk.tsv"):
            species = file.replace("_hrs_hk.tsv", "")
            input_path = os.path.join(proteomes_hrs_hk, file)
            output_path = os.path.join(output_dir, f"{species}_length.tsv")
            print("processing", species)

            if species in gtf_id_keys:
                gtf_path = f"{INPUT_BASE_DIR}/gtf_files/gtf_genbank_{species}.gtf"
                id_key = gtf_id_keys[species]
                Genelength_from_gtf(gtf_path, id_key=id_key)
                match_by_gene_name = True
                force_upper = not case_sensitive_lookup.get(species, True)
            else:
                biomart_file = f"{species}_biomart.txt"
                biomart_path = os.path.join(biomart_dir, biomart_file)
                Genelength(biomart_path)
                match_by_gene_name = False
                force_upper = False

            Create_genelength_doc(input_path, output_path, match_by_gene_name=match_by_gene_name, force_upper=force_upper)
        else:
            print(f"wrong file name: {file}")

proteomes_hrs_hk = f"{REP_BASE_DIR}/analysis/proteomes_hrs_hk"
biomart_dir = f"{REP_BASE_DIR}/analysis/biomart"
output_dir = f"{REP_BASE_DIR}/analysis/genelengthoutput"

Process_genelength(proteomes_hrs_hk, biomart_dir, output_dir)