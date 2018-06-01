######################################################
# Please do not edit this file.                      #
# Contents of this file will be overwritten when the #
# project is closed.                                 #
######################################################
prefer fitenhance=true fitenhancenear=29.5909 fitenhancefar=-29.5909
ribbon display=ribbonsonly
hbondcriteria display=false displayhbond=true displayhalogen=true displaysaltbridge=true displayaromatichbond=false distance=2.8 donorangle=120 acceptorangle=90 halogendistance=3.5 donorminimumangleasdonor=140 acceptorminimumangleasdonor=90 donorminimumangleasacceptor=120 acceptorminimumangleasacceptor=90 acceptormaximumangleasacceptor=170 saltbridgedistance=5 aromatichbonddistance_o=2.8 aromatichbonddistance_n=2.5 aromatichbonddonorminangle_o=90 aromatichbonddonorminangle_n=108 aromatichbonddonormaxangle_n=130 aromatichbondacceptorminangle=90
displayhbondsmode  mode=ligandreceptor
hbondset2 (( (( ( entry.id 216 223 59 ) ) AND ( ( m.n 1 ) OR ( m.n 136) )) ) or ( (( (( ( entry.id 216 223 59 ) ) AND ( water )) ) AND ( within 4 ( (( ( entry.id 216 223 59 ) ) AND ( ( m.n 1 ) OR ( m.n 136) )) ) )) ))
hbondset1 (( (( ( entry.id 216 223 59 ) ) AND ( (backbone) or (sidechain) )) ) or ( (( (( ( entry.id 216 223 59 ) ) AND ( water )) ) AND ( within 4 ( (( ( entry.id 216 223 59 ) ) AND ( ( m.n 1 ) OR ( m.n 136) )) ) )) ))
contactcriteria display=true displaygood=false displaybad=true displayugly=true good=1.3 bad=0.89 ugly=0.75 excludehbond=true
displaycontactsmode  mode=ligandreceptor
contactset2 (protein_near_ligand) or (water and within 5.0 ligand)
contactset1 (ligand) or (water and within 5.0 ligand)
displaypiinteractions display=true displaystacking=true displaycation=true
displaypiinteractionsmode  mode=ligandreceptor
piinteractionset2 (protein_near_ligand) or (water and within 5.0 ligand)
piinteractionset1 (ligand) or (water and within 5.0 ligand)
clip front=-163.251 back=-338.03 frontsurface=-163.251 backsurface=-338.03 leftsurface=27.1396 rightsurface=201.918 leftslopesurface=0 rightslopesurface=0 frontselect=-163.251 backselect=-338.03 boxoffset=0 objects=all
prefer annotationsvisible=true interactionsvisible=false measurementsvisible=true ribbonsvisible=true surfacesvisible=true