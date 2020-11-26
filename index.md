# Title: Hardy *et al.* (2020) Molecular modeling of inhibtors of mitochondrial complex 1

## Author: Yizhou Yu, yzy21 [at] mrc-tox.cam.ac.uk

### Affiliation: MRC Toxicology Unit, University of Cambridge

### Date: 10 June 2020

## General information

This pipeline relates to data and analysis included in Figures X of our study titled XX.

Here, we dock different ligands to C1, at ONLY the Q site, on the Open conformation, to investigate competitive binding. The receptor structure is named AllCxI_Q10.pbd, which is a simulated structure by Hirst *et al.* (PNAS, 2016). We renamed it to hirst_C1_o.pdb after cleaning. Calculations are performed using Autodock Vina at 200 exhaustiveness, which is the max allowed by the HPC. 

The docking script creates the preparation files for docking on a Linux-based HPC, using a simple loop to run everything. They are in the folder call ari_rot_pieri_hpc_docked, along with the raw data.

The input files for this analysis pipeline are on the master branch of this GitHub page: 
https://github.com/M1gus/Aripiprazole

The file Ki_calculations_from_deltaG.R contains a script to convert the deltaG values obtained from Autodock Vina to inhibition constants(Ki). 

The raw and processed PDB coordinates of respiratory complex 1 are in raw_structures and processed_structures, respectively. Below is an example of preprocessing the PDB files. It also contains detailed notes for the subsequent docking calculations using Autodock Vina and visualisation using Pymol. 

## Example code for preprocessing


```bash
# take away the U10 and NADP ligands

awk '$4!="U10"' raw_structures/hirst_C1_o.pdb > processed_structures/hirst_C1_o_clean.pdb
```

NB: I took out the FMN, NADP, HSD, U10, ZN2 molecules by hand on pymol since there were problems with how it is coded, in the hirst_C1_o_clean file. Below is an example for preprocessing the PDB files for docking with Autodock Vina.


```bash
/Library/MGLTools/1.5.7rc1/bin/pythonsh ../python_programs/prepare_receptor4.py -r processed_structures/hirst_C1_o_clean.pdb -e -d hirst_C1_o_preparation.txt

```

    setting PYTHONHOME environment
    Unable to assign MAP type to atom N
    Sorry, there are no Gasteiger parameters available for atom hirst_C1_o_clean:S:HSD21:NE2
    Sorry, there are no Gasteiger parameters available for atom hirst_C1_o_clean:S:GLU56:OE1
    'Deleting non-standard residues:BHSD61_BHSD127_CHSD19_CHSD53_CHSD67_CHSD145_CHSD160_DHSD27_DHSD55_DHSD79_DHSD84_DHSD150_DHSD157_DHSD190_DHSD200_DHSD347_DHSD348_DHSD398_DHSD409_EHSD9_EHSD42_EHSD99_FHSD29_FHSD113_FHSD116_FHSD261_FHSD283_FHSD356_FHSD402_FHSD421_FHSD437_GHSD43_GHSD101_GHSD255_GHSD293_GHSD401_GHSD421_GHSD437_GHSD494_GHSD548_GHSD549_HHSD247_HHSD250_HHSD287_HHSD304_IHSD65_IHSD144_KHSD25_KHSD52_LHSD56_LHSD67_LHSD230_LHSD248_LHSD328_LHSD332_LHSD348_LHSD514_LHSD534_LHSD605_MHSD30_MHSD82_MHSD83_MHSD187_MHSD213_MHSD220_MHSD293_MHSD319_MHSD338_MHSD422_MHSD440_NHSD25_NHSD48_NHSD112_NHSD186_NHSD232_NFES301_NFES803_NSF4201_NSF4502_NSF4802_NSF4801_NSF4202_OHSD57_OHSD114_OHSD151_OHSD167_OHSD190_OHSD257_OHSD287_PHSD2_PHSD3_PHSD8_PHSD37_PHSD49_PHSD58_PHSD87_PHSD131_PHSD134_PHSD250_PHSD260_PHSD288_PHSD296_PHSD321_QHSD29_RHSD13_RHSD68_SHSD21_SHSD27_SHSD40_SHSD68_SHSD9_SHSD35_SHSD59_SHSD88_SHSD97_SHSD26_SHSD33_SHSD44_SHSD76_SHSD10_SHSD13_SHSD45_SHSD103_SHSD63_SHSD69_SHSD124_SHSD135_SHSD66_SHSD73_SHSD82_SHSD42_SHSD50_SHSD78_SHSD104_SHSD11_SHSD25_SHSD32_SHSD72_SHSD75_SHSD107_SHSD168_SHSD60_SHSD81_SHSD84_SHSD91_SHSD55_SHSD64_SHSD120_SHSD143_SHSD148_SHSD17_SHSD87_SHSD113_SHSD46_THSD35_UHSD35_VHSD20_VHSD36_WHSD47_WHSD71_WHSD101_WHSD107_WHSD125_XHSD29_XHSD30_XHSD76_XHSD142_XHSD162_YHSD18_ZHSD111_ from hirst_C1_o_clean



```bash
/Library/MGLTools/1.5.7rc1/bin/pythonsh ../python_programs/prepare_ligand4.py -l raw_structures/piericidinA.pdb -o processed_structures/piericidinA.pdbqt
/Library/MGLTools/1.5.7rc1/bin/pythonsh ../python_programs/prepare_ligand4.py -l raw_structures/rotenone.pdb -o processed_structures/rotenone.pdbqt

```

    setting PYTHONHOME environment
    setting PYTHONHOME environment



```bash
#also include the original U10 for docking 

/Library/MGLTools/1.5.7rc1/bin/pythonsh ../python_programs/prepare_ligand4.py -l raw_structures/U10_from_hirst.pdb -o processed_structures/U10_hirst.pdbqt
```

    setting PYTHONHOME environment


## Notes on docking using Autodock Vina

For docking at the Q site: <br>
`center_x = 73.6025098`

`center_y = -6.034084967`

`center_z = 23.58526797`

The size of the Q site is 13 x 21 x 39. By having a search space of 30 * 40 * 70, I am sure to cover the correct search area. These calcualtions were done on Excel: U10_from_hirst.xls. 

All files are sent to a Linux-based high performance computing cluster for the calculations. 

## Visualisation in Pymol

The nearest chains to the U site are D, B and H (all in capital)

In the figure, I used the same solor scheme as here: https://www.nature.com/articles/nature19095/figures/3 <br>
According to Hirst's Nature 2016 paper, 
- PSST is NDUFS7 -> chain B (green - 7CAE00)
- 49kDa is NDUFS2 -> chain D (blue - 00BFC4)
- ND1 is NADH-ubiquinone oxidoreductase chain 1	-> chain H (red - F8766D)
<br>
U10 in blue: R=0 G=150 B=247 -> 0096f7<br>
Toxic molecules in red: R=236 G=28 B=36 -> ec1c24 <br>

