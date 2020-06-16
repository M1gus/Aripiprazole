for receptor in mitoC1*.pdbqt
do
for ligand in lig_*.pdbqt
do ./vina --ligand $ligand --receptor $receptor --log log_${ligand%.*}_${receptor%.*}_500.txt --config *config.txt --out out__${ligand%.*}_${receptor%.*}_500.pdbqt
done
done