version of Reference Proteomes: 2024/06
version of virushostdb.tsv (downloaded March 3rd 2025): 2025-01-27


# counts of supergroup	# organisms	# proteins
Phages	4894	445674
Unknown	4825	59553
Viruses	3078	66200

Eukaryotes	2463	39696894
Eukaryotic hosts	302	6962467

Prokaryotes	9249	35505440
Prokaryotic hosts	144	542224


HR category	supergroup	num_proteins	num_organisms
0	Eukaryotic hosts	6461575	302
1	Eukaryotic hosts	384441	302
2	Eukaryotic hosts	70307	301
>2	Eukaryotic hosts	46144	300

0	Prokaryotic hosts	538918	144
1	Prokaryotic hosts	3043	144
2	Prokaryotic hosts	205	80
>2	Prokaryotic hosts	58	41

0	Viruses	63621	3067
1	Viruses	2101	482
2	Viruses	344	143
>2	Viruses	134	58

0	Phages	442706	4894
1	Phages	2388	1621
2	Phages	394	369
>2	Phages	186	180



# Header by columns:
[1:proteome_id] [2:species] [3:tax_id] [4:protein_count] [5:lineage] [6:group_of_organism] [7:uniprot_file_path] [8:superregnum] [9:manually_added] [10:host_group] [11:supergroup]

# Example of a line by columns:
[1|proteome_id|UP000002199]
[2|species|Archaeoglobus fulgidus (strain ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 / VC-16)]
[3|tax_id|224325]
[4|protein_count|2394]
[5|lineage|cellular organisms, Archaea, Methanobacteriati, Methanobacteriota, Archaeoglobi, Archaeoglobales, Archaeoglobaceae, Archaeoglobus, Archaeoglobus fulgidus]
[6|group_of_organism|Archaea]
[7|uniprot_file_path|Archaea/UP000002199/UP000002199_224325.fasta.gz]
[8|superregnum|Archaea]
[9|manually_added|0]
[10|host_group|Archaea]
[11|supergroup|Prokaryotes]


# Methods:
Viruses were classified in Viruses and Phages based on host lineage information obtained from Virust-Host DB (version 2025-01-27). The classification process involved parsing the host lineage string for each proteome and assigning it to one of the predefined categories: Bacteria, Archaea, Fungi, Plants, Vertebrates, or Invertebrates. The categories were assigned using a hierarchical decision tree. Metazoa were assigned to Invertebrates if 'Vertebrata' is not found in the lineage.
The host group is documented in the column host_group. If the host belonged to Archaea or Bacteria, the Virus was classified as Phage. If the host belongs to a eukaryotic group, the Virus was classified as Virus.
Eukaryotes and Prokaryotes were classified as hosts if the tax id was found in the column "host tax id" in virushostdb.tsv.
The classification into Viruses, Phages, Eukaryotic hosts, Eukaryotes, Prokaryotic hosts and Prokaryotes is documented in the column supergroup.

> Archaea  = ['Archaea']
> Bacteria = ['Bacteria']
> Protists = ['Sar', 'Amoebozoa', 'Apusozoa', 'Cryptophyceae', 'Discoba', 'Haptista', 'Metamonada', 'Choanoflagellata', 'Filasterea', 'Ichthyosporea', 'Rotosphaerida']
> Fungi    = ['Fungi']
> Plants = ['Viridiplantae', 'Rhodophyta']
> Vertebrates = ['Vertebrata']
> Invertebrates = ['Metazoa']	# if not Vertebrates
