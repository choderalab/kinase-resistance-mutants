# Script to renumber PDBs in the Hauser benchmark set
# Steven K. Albanese, with copious help from Stack overflow posts by Gordon Wells and Maximillian Peters

from Bio import AlignIO,SeqIO,ExPASy,SwissProt
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
from Bio import pairwise2
from Bio.SubsMat.MatrixInfo import blosum62

import os
from Bio import PDB
import argparse

# Skeleton command line interface in case that is the easiest way to use the script
parser = argparse.ArgumentParser(description="Automated script to search PDB by chemical ID")
parser.add_argument('--input', required=True, dest='pdb_file',
                    help='THe pdb file that you would like to run through this program')
args = parser.parse_args()

file_name = args.pdb_file


cap = True  # Set this to false if there are no cap residues


pdb_io = PDB.PDBIO()
# Read in PDB file
id_name = file_name
pdb_name = file_name + '.pdb'
parser = PDB.PDBParser(PERMISSIVE=1)
structure = parser.get_structure(id_name, pdb_name)

# Extract sequence from PDB file and skip cap residues (which won't align properly)
oneletter = {
    'ASP': 'D', 'GLU': 'E', 'ASN': 'N', 'GLN': 'Q',
    'ARG': 'R', 'LYS': 'K', 'PRO': 'P', 'GLY': 'G',
    'CYS': 'C', 'THR': 'T', 'SER': 'S', 'MET': 'M',
    'TRP': 'W', 'PHE': 'F', 'TYR': 'Y', 'HIS': 'H',
    'ALA': 'A', 'VAL': 'V', 'LEU': 'L', 'ILE': 'I',
}

cap_res = ['NME', 'NMA', 'ACE']

pdbseq_list = []
for residue in structure.get_residues():
    three_letter = residue.get_resname()
    if three_letter in cap_res:
        pass
    else:
        one_letter_name = oneletter[three_letter]
        pdbseq_list.append(one_letter_name)

pdbseq_str = ''.join(pdbseq_list)

# Write out FASTA file for PDB structure
alnPDBseq=SeqRecord(Seq(pdbseq_str,IUPAC.protein),id=file_name)
SeqIO.write(alnPDBseq,"%s.fasta"%file_name,"fasta")

# Retrieve reference sequence
accession = "P00519"  # eventually this can be specified by user somehow (or read in from the csv file)
handle = ExPASy.get_sprot_raw(accession)
swissseq = SwissProt.read(handle)
refseq=SeqRecord(Seq(swissseq.sequence,IUPAC.protein),id=accession)
SeqIO.write(refseq, "%s.fasta"%accession,"fasta")

# Align using Biopython's EMBOSS needle wrapper
seq1 = SeqIO.read("%s.fasta"% accession, "fasta")  # Uniprot  sequence
seq2 = SeqIO.read("%s.fasta"% file_name, "fasta")  # PDB sequence

alignments = pairwise2.align.localds(seq1.seq, seq2.seq, blosum62, -10, -0.5)
alignment_start = alignments[0][3]
alignment_end = alignments[0][4]

# Clean up FASTA files
os.remove("%s.fasta"%file_name)
os.remove("%s.fasta"%accession)

# Create the list of new residue numbers from the alignment
new_resnums = list(range(alignment_start, alignment_end+1))


# Renumber the residue IDs in the structure
for i, residue in enumerate(structure.get_residues()):
    three_letter = residue.get_resname()
    if three_letter == 'ACE':  # Set resid for ACE to 1 before the start of the alignment
        res_id = list(residue.id)
        res_id[1] = new_resnums[0] - 1
        residue.id = tuple(res_id)
    elif three_letter == 'NME' or three_letter == 'NMA':  # Set resid for NME or NMA to 1 after the end of the alignment
        res_id = list(residue.id)
        res_id[1] = new_resnums[-1] + 1
        residue.id = tuple(res_id)
    else:
        if cap:
            index = i - 1
        else:
            index = i
        res_id = list(residue.id)
        res_id[1] = new_resnums[index]
        residue.id = tuple(res_id)

#  Write the renumbered PDB file
pdb_io = PDB.PDBIO()
pdb_io.set_structure(structure)
pdb_io.save(file_name + "-renumbered.pdb")