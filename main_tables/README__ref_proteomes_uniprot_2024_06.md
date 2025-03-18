The column fasta_file_path = root_path + uniprot_file_path, where:
- root_path = ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Reference_Proteomes_2024_06/
- uniprot_file_path = Viruses/UP000000400/UP000000400_652669.fasta.gz (file_path differs for each proteome)


version of Reference Proteomes: 2024/06
version of Lineage (downloaded February 17 2025): 2025/01 (taxonomy is updated only at UniProt releases)

# counts of proteomes
24955 ref_proteomes_uniprot_2025_01
24955 proteomes in uniprot (2024/06)


# Header by columns:
[1:proteome_id] [2:species] [3:tax_id] [4:protein_count] [5:lineage] [6:group_of_organism] [7:uniprot_file_path] [8:superregnum] [9:manually_added]

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


# counts of superregnum:
 12797 Viruses
   303 Archaea
  9090 Bacteria
  2765 Eukaryota

# counts of group_of_organism:
12797 Viruses
  303 Archaea
 9090 Bacteria
 1222 Fungi
  302 Plants
  200 Protists    
  388 Invertebrates
  653 Vertebrates


Methods:
Organisms were classified into major taxonomic groups based on lineage information obtained from UniProt (release 2025/01). The classification process involved parsing the lineage string for each proteome and assigning it to one of the predefined categories: Bacteria, Viruses, Archaea, Fungi, Plants, Vertebrates, or Invertebrates. The categories were assigned using a hierarchical decision tree. Metazoa were assigned to Invertebrates if 'Vertebrata' is not found in the lineage. A total of 14 organisms required manual adjustments due to discrepancies between UniProt versions.

> Viruses  = ['Viruses']
> Archaea  = ['Archaea']
> Bacteria = ['Bacteria']
> Protists = ['Sar', 'Amoebozoa', 'Apusozoa', 'Cryptophyceae', 'Discoba', 'Haptista', 'Metamonada', 'Choanoflagellata', 'Filasterea', 'Ichthyosporea', 'Rotosphaerida']
> Fungi    = ['Fungi']
> Plants = ['Viridiplantae', 'Rhodophyta']
> Vertebrates = ['Vertebrata']
> Invertebrates = ['Metazoa']	# if not Vertebrates


Due to changes between the releases 2024/06 and 2025/01, 14 organisms had to be added manually to the file:
organism_id	reason
UP000216052	not in lineage file (proteome excluded)
UP000216752	not in lineage file (proteome excluded)
UP000294981	not in lineage file (proteome excluded)
UP000293303	not in lineage file (proteome excluded)
UP000003242	different tax id in reference proteome and lineage file
UP000586722	different tax id in reference proteome and lineage file
UP000510647	different tax id in reference proteome and lineage file
UP000000561	different tax id in reference proteome and lineage file
UP000197619	different tax id in reference proteome and lineage file
UP000218220	not in lineage file (proteome excluded)
UP000504620	not in lineage file (proteome excluded)
UP000006543	different tax id in reference proteome and lineage file
UP000008236	different tax id in reference proteome and lineage file
UP000008665	not in lineage file (proteome excluded)

Info on manually added organisms:
UP000216052	Sporomusa acidovorans DSM 3132	1123286	5767	cellular organism, Bacteria, Bacillati, Bacillota, Negativicutes, Selenomonadales, Sporomusaceae, Sporomusa, Sporomusa acidovorans	Bacteria	Bacteria/UP000216052/UP000216052_1123286.fasta.gz	Bacteria	1
UP000216752	Sporomusa silvacetica DSM 10669	1123289	5636	cellular organism, Bacteria, Bacillati, Bacillota, Negativicutes, Selenomonadales, Sporomusaceae, Sporomusa, Sporomusa silvacetica	Bacteria	Bacteria/UP000216752/UP000216752_1123289.fasta.gz	Bacteria	1
UP000294981	Streptomyces sp. KM273126	2545247	8325	cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Kitasatosporales, Streptomycetaceae, Streptomyces, unclassified Streptomyces	Bacteria	Bacteria/UP000294981/UP00029498_2545247.fasta.gz	Bacteria	1
UP000293303	Cryobacterium sp. SO1	1897061	3761	cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Micrococcales, Microbacteriaceae, Cryobacterium	Bacteria	Bacteria/UP000293303/UP000293303_1897061	Bacteria	1
UP000003242	Megasphaera lornae	1000568	1610	cellular organisms, Bacteria, Bacillati, Bacillota, Negativicutes, Veillonellales, Veillonellaceae, Megasphaera	Bacteria	Bacteria/UP000003242/UP000003242_699218.fasta.gz	Bacteria	1
UP000586722	Pannonibacter tanglangensis	2750084	3898	cellular organisms, Bacteria, Pseudomonadota, Alphaproteobacteria, Hyphomicrobiales, Stappiaceae, Pannonibacter	Bacteria	Bacteria/UP000586722/UP000586722_2750085.fasta.gz	Bacteria	1
UP000510647	Torulaspora globosa	48254	4924	cellular organisms, Eukaryota, Opisthokonta, Fungi, Dikarya, Ascomycota, saccharomyceta, Saccharomycotina, Saccharomycetes, Saccharomycetales, Saccharomycetaceae, Torulaspora	Fungi	Eukaryota/UP000510647/UP000510647_2792677.fasta.gz	Eukaryota	1
UP000000561	Mycosarcoma maydis (Corn smut fungus) (Ustilago maydis)	5270	6805	cellular organisms, Eukaryota, Opisthokonta, Fungi, Dikarya, Basidiomycota, Ustilaginomycotina, Ustilaginomycetes, Ustilaginales, Ustilaginaceae, Mycosarcoma	Fungi	Eukaryota/UP000000561/UP000000561_237631.fasta.gz	Eukaryota	1
UP000197619	Lonchura striata (white-rumped munia)	40157	15252	cellular organisms, Eukaryota, Opisthokonta, Metazoa, Eumetazoa, Bilateria, Deuterostomia, Chordata, Craniata, Vertebrata, Gnathostomata, Teleostomi, Euteleostomi, Sarcopterygii, Dipnotetrapodomorpha, Tetrapoda, Amniota, Sauropsida, Sauria, Archelosauria, Archosauria, Dinosauria, Saurischia, Theropoda, Coelurosauria, Aves, Neognathae, Neoaves, Telluraves, Australaves, Passeriformes, Passeroidea, Estrildidae, Estrildinae, Lonchura	Vertebrates	Eukaryota/UP000197619/UP000197619_299123.fasta.gz	Eukaryota	1
UP000218220	Heliothis virescens	7102	14951	cellular organisms, Eukaryota, Opisthokonta, Metazoa, Eumetazoa, Bilateria, Protostomia, Ecdysozoa, Panarthropoda, Arthropoda, Mandibulata, Pancrustacea, Hexapoda, Insecta, Dicondylia, Pterygota, Neoptera, Endopterygota, Amphiesmenoptera, Lepidoptera, Glossata, Neolepidoptera, Heteroneura, Ditrysia, Obtectomera, Noctuoidea, Noctuidae, Heliothinae, Heliothis	Invertebrates	Eukaryota/UP000218220/UP000218220_7102.fasta.gz	Eukaryota	1
UP000504620	Bicyclus anynana	110368	14373	cellular organisms, Eukaryota, Opisthokonta, Metazoa, Eumetazoa, Bilateria, Protostomia, Ecdysozoa, Panarthropoda, Arthropoda, Mandibulata, Pancrustacea, Hexapoda, Insecta, Dicondylia, Pterygota, Neoptera, Endopterygota, Amphiesmenoptera, Lepidoptera, Glossata, Neolepidoptera, Heteroneura, Ditrysia, Obtectomera, Papilionoidea, Nymphalidae, Satyrinae, Satyrini, Mycalesina, Byciclus	Invertebrates	Eukaryota/UP000504620/UP000504620_110368.fasta.gz	Eukaryota	1
UP000006543	Subterranean clover stunt C6 alphasatellite (SCSC6A)	1458459	1	Viruses, Alphasatellitidae, Nanoalphasatellitinae, Clostunsatellite, Subterranean clover stunt alphasatellite 2	Viruses	Viruses/UP000006543/UP000006543_291607.fasta.gz	Viruses	1
UP000008236	Milk vetch dwarf C10 alphasatellite (MVDC10A)	1455652	1	Viruses, Alphasatellitidae, Nanoalphasatellitinae, Milvetsatellite, Milk vetch dwarf alphasatellite 3	Viruses	Viruses/UP000008236/UP000008236_291605.fasta.gz	Viruses	1
UP000008665	Faba bean necrotic yellows virus (isolate Egyptian EV1-93)	291603	11	Viruses, Monodnaviria, Shotokuvirae, Cressdnaviricota, Arfiviricetes, Mulpavirales, Nanoviridae, Nanovirus, Faba bean necrotic yellows virus	Viruses	Viruses/UP000008665/UP000008665_291603.fasta.gz	Viruses	1
