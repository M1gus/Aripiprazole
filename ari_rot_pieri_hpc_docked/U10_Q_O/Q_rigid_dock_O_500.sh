for receptor in mitoC1*.pdbqt
do
for ligand in lig*.pdbqt
do ./vina --ligand $ligand --receptor $receptor --log log_${ligand%.*}_${receptor%.*}_70A_500.txt --config *config.txt --out out__${ligand%.*}_${receptor%.*}_70A_500.pdbqt
done
done
