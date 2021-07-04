for receptor in r_*.pdbqt
do
for ligand in l_*.pdbqt
do 
for config in *_config.txt
do
./vina --ligand $ligand \
--receptor $receptor \
--log log_${ligand%.*}_${receptor%.*}_${config%_*}.txt \
--config $config --out out_${ligand%.*}_${receptor%.*}_${config%_*}.pdbqt
done
done
done
