
"""
Data importation methods
"""

# standard libraries
import os 
import urllib
import warnings

# nonstandard libraries
import pandas as pd
from Bio.PDB import *
from Bio import BiopythonWarning

# homegrown libraries

# library modifications
warnings.simplefilter('ignore', BiopythonWarning)

# --------------------- #

def _read_files(fname):
    
    """ Reads PDB name from .csv file """
   
    column_id = "IMGT entry ID" 
   
    df = pd.read_csv(fname)
    pdb_names = [d for d in df[column_id]]

    print '{} PDB files listed.'.format(len(pdb_names))
    
    return pdb_names

# --------------------- #

def _load_pdb_files(pdb_names):

    """ Download PDB files listed in iterable"""

    # fix input if string
    if isinstance(pdb_names,str): pdb_names = [pdb_names]

    # dictionary for data
    pdb_files = {}

    # iterate each file
    for i,pdb_name in enumerate(pdb_names):
        pdb_files[pdb_name] = _load_pdb_file(pdb_name)
        if i%10 == 9 and i != 0: print '{} PDBs loaded.'.format(len(pdb_files))

    return pdb_files

# --------------------- #

def _load_pdb_file(pdb_name):

    pdb_name = pdb_name.lower()

    # check if save folder exists
    if not os.path.isdir('structures'):
            os.makedirs('structures')
    
    fname = 'structures/{}.pdb'.format(pdb_name)


    if os.path.exists(fname):
        with open(fname,'r') as f:
            return f.read()
    
    # load from URL if not previously downloaded
    else:
        url = 'http://www.rcsb.org/pdb/files/{}.pdb'.format(pdb_name)
        data = urllib.urlopen(url).read()
        with open(fname,'w') as f:
            f.write(data)
        return data


# --------------------- #

def import_data(fname):
    pdb_names = _read_files(fname)
    pdb_files = _load_pdb_files(pdb_names)
    return pdb_files
    

    #print val
    #print dir(val)
