# Modified slightly from the Modeller manual example

# Imports
import modeller


build_method = 'INTERNAL_COORDINATES' # Controls which method gets used to build missing coordinates in. The options are 'INTERNAL_COODRINATES, '3D_Interpolation', 'ONE_STICK' or 'TWO_STICK'

# Initialize environ, load in parameters and point to atom files (PDBs)
env = modeller.environ()
env.io.atom_files_directory = ['input'] # This needs to point to directory containing the input PDB files
env.libs.topology.read(file='$(LIB)/top_heav.lib') #This set of parameters will only build in heavy atoms. Use '$(LIB)/top_allh.lib' to add in hydrogens
env.libs.parameters.read(file='$(LIB)/par.lib') # These are modified CHARMM22 parameters.

code='cAbl-imatinib_nowat-uniprot.pdb' # This needs to be the name of the PDB file we want loaded in

aln = modeller.alignment(env)
mdl = modeller.model(env, file=code)
mdl_original = modeller.model(env, file=code)

aln.append_model(mdl, atom_files=code, align_codes=code) # Passing the same PDB file to both atom_files and align_codes seems to work

sel = modeller.selection(mdl.chains['B'].residues[87]) # This is the index of the residue
sel.mutate(residue_type='ILE') # Normal three letter codes are supported here
aln.append_model(mdl, align_codes='mut')
mdl.clear_topology()
mdl.generate_topology(aln['mut'])
mdl.transfer_xyz(aln)
mdl.build(initialize_xyz=False, build_method=build_method)
mdl.res_num_from(mdl_original, aln)
mdl.write(file='mut.pdb') # This could probably be changed to output file name. File type appears to be controlled by the suffix
