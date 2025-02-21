version of uniprot: 2024/06
version of Lineage (downloaded): 2025/01 (taxonomy is updated only at UniProt releases)

# counts of proteomes
24952 ref_proteomes_uniprot_2025_01 + 3 viruses
24955 proteomes in uniprot


# Header by columns:
[1:proteome_id] [2:species] [3:tax_id] [4:protein_count] [5:lineage] [6:group_of_organism] [7:uniprot_file_path] [8:superregnum]

# Example of a line by columns:
[1|proteome_id|UP000002199]
[2|species|Archaeoglobus fulgidus (strain ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 / VC-16)]
[3|tax_id|224325]
[4|protein_count|2394]
[5|lineage|cellular organisms, Archaea, Methanobacteriati, Methanobacteriota, Archaeoglobi, Archaeoglobales, Archaeoglobaceae, Archaeoglobus, Archaeoglobus fulgidus]
[6|group_of_organism|Archaea]
[7|uniprot_file_path|Archaea/UP000002199/UP000002199_224325.fasta.gz]
[8|superregnum|Archaea]


# counts of superregnum:
 12794+3 Viruses
   303 Archaea
  9090 Bacteria
  2765 Eukaryota

# counts of group_of_organism:
12794+3 Viruses
  303 Archaea
 9090 Bacteria
 1222 Fungi
  305 Plants
  197 Protists    
  388 Invertebrates
  653 Vertebrates


Due to changes between the releases 2024/06 and 2025/01, 14 organisms had to be added manually to the file:
organism_id	reason
UP000003242	different tax id in reference proteome and lineage file
UP000216052	not in lineage file (proteome excluded)
UP000216752	not in lineage file (proteome excluded)
UP000293303	not in lineage file (proteome excluded)
UP000294981	not in lineage file (proteome excluded)
UP000586722	different tax id in reference proteome and lineage file
UP000000561	different tax id in reference proteome and lineage file
UP000197619	different tax id in reference proteome and lineage file
UP000218220	not in lineage file (proteome excluded)
UP000504620	not in lineage file (proteome excluded)
UP000510647	different tax id in reference proteome and lineage file
Virus 1
Virus 2
Virus 3


Methods:  
> Viruses  = ['Viruses']
> Archaea  = ['Archaea']
> Bacteria = ['Bacteria']
> Protists = ['Alveolata', 'Amoeboza', 'Apusozoa', 'Bigyra', 'Cryptophyceae', 'Discoba', 'Haptista', 'Metamonada', 'Ochrophyta', 'Oomycota', 'Opisthokonta', 'Rhizaria']
> Fungi    = ['Fungi']
> Plants = ['Viridiplantae', 'Rhodophyta', 'Phaeopyceae', 'Xanthophyceae']
> Vertebrates = ['Vertebrata']
> Invertebrates = ['Metazoa']	#  if not Vertebrates
