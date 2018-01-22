## Manifest

* `ligands` - the .mol2 and .sdf files for each of the ligands 
* `receptors` - converted PDB files using the original number in the .mae files 
* `renumbered_receptors` - converted PDB files aligned to the uniprot sequence for Abl (accession ID: P00519) 	

### Protocol to convert 

The .mae files from this paper were loaded into Maestro (2017-4) and seperated by using the `split into protein, ligand, waters` function. Proteins and waters were merged back into the same file prior to merging if denoted `wat`. 

Uniprot renumbering was performed using the script `renumber_pdbs.py`. Shortly, The sequence was extracted from each PDB file, and aligned to the Uniprot sequence (Accession id P00519). N-terminal caps were numbered First Residue - 1. C-terminal caps were numbered Last Residue+A, and renamed to NME. 
