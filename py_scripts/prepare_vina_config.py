'''
Author: Yizhou Yu
Usage: 
This scripts takes the the location of a ligand or residue
and outputs the vina config file at num_mode = 10,
exhaustiveness = 100. The search center is the center of the
input file. The area of search is the the box of the ligand
adding 5A each side

Example: python3 py_scripts/prepare_vina_config.py -l $file
'''

import os
import re
import subprocess
import sys
import math
import numpy as np
import argparse
import itertools
import operator
from Bio.PDB import * #imports all 

#sys.path.insert(0,"/Documents/pymol/bin")


length_x = 0

def make_config_file(ligand):
  # Get the atoms for the receptor & store in numpy
  bioparser = PDBParser()
  #A_coordinates = np.array([])
  #assume 1 model (iteration of whole protein), but allows multiple chains
  with open(str(''.join(ligand)), 'r') as infile:
    #get a parser i.e. interpreter for PDB files 
    ligand_structure = bioparser.get_structure("protein_structure", infile)
    for model in ligand_structure:
        xmin_model = 999999999.0
        xmax_model = -xmin_model
        ymin_model = 999999999.0
        ymax_model = 0.0
        zmin_model = 999999999.0
        zmax_model = 0.0
        count = 0
        for chain in model:
            for residue in chain:
                for atom in residue:
                  x_coord,y_coord,z_coord = atom.get_coord()
                  if x_coord < xmin_model: xmin_model = x_coord
                  if x_coord > xmax_model: xmax_model = x_coord
                  if y_coord < ymin_model: ymin_model = y_coord
                  if y_coord > ymax_model: ymax_model = y_coord
                  if z_coord < zmin_model: zmin_model = z_coord
                  if z_coord > zmax_model: zmax_model = z_coord 
                  #print(x_coord,y_coord,z_coord)
         
        length_x = round(xmax_model - xmin_model)
        length_y = round(ymax_model - ymin_model)
        length_z = round(zmax_model - zmin_model)
        #print "min, max x, width = ",xmin_model, xmax_model, length_x
        #now that I obtained the "box size of the protein," I need to find the center of the box
        center_x = round(xmax_model-(length_x/2))
        center_y = round(ymax_model-(length_y/2))
        center_z = round(zmax_model-(length_z/2))
        size_string = "center_x = " + str(center_x) + "\n" + \
                      "center_y = " + str(center_y) + "\n" + \
                      "center_z = " + str(center_z) + "\n" + \
                      "size_x = " + str(length_x*2) + "\n" + \
                      "size_y = " + str(length_y*2) + "\n" + \
                      "size_z = " + str(length_z*2)
        print(size_string)
        print("\n")
        print("num_modes = 10\n\nexhaustiveness = 300")
            
parser = argparse.ArgumentParser(description='Produce a standard config file for Vina')
parser.add_argument('-l', '--ligand', required=True, nargs='+')
args = parser.parse_args()

if __name__ == '__main__': 
    make_config_file(args.ligand)

