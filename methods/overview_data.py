

"""
Overview the data properties
"""

# standard libraries
import warnings
import itertools

# nonstandard libraries
import matplotlib.pyplot as plt
from Bio.PDB import *
from Bio import BiopythonWarning
from Bio import pairwise2

# homegrown libraries

# library modifications
warnings.simplefilter('ignore', BiopythonWarning)

# --------------------- #

def chain_length_frequency(pdb_files):

    pdbp = PDBParser()
    ppb = PPBuilder()

    chain_lengths = []
    
    
    for i,pdb in enumerate(pdb_files.keys()): # iterate through structures
        structure = pdbp.get_structure('test','structures/' + pdb + '.pdb')
        for pp in ppb.build_peptides(structure): # iterate through chains
            chain_lengths.append(len(pp.get_sequence()))
        if i%10 == 9 and i != 0: print '{} PDBs extracted.'.format(i)

    # plot sequence lengths
    plt.hist(chain_lengths,bins=40)
    plt.xlabel('Chain lengths in all structures')
    plt.ylabel('Frequency (#)')
    
    # display resulting plot
    plt.show(block=False)
    raw_input('Press enter to close...')
    plt.close()

# --------------------- #

def hamming_dist(s1,s2):
    assert len(s1) == len(s2),"lengths not equivalent between strings"
    return 1. - float(sum(itertools.imap(str.__ne__, s1, s2)))/len(s1)

# --------------------- #

def _get_sequences_from_pdb_files(pdb_files):

    pdb_seqs = {}
    pdbp,ppb  = PDBParser(),PPBuilder()

    for k,v in pdb_files.items()[:10]:

        ss = pdbp.get_structure('test','structures/' + k + '.pdb')
        pdb_seqs[k] = [pp.get_sequence() for pp in ppb.build_peptides(ss)] # iterate through chains

    return pdb_seqs

# --------------------- #

def alignment(pdb_files):

    homology_dict = {
            'MHC':'GPHSMRYYETATSRRGLGEPRYTSVGYVDDKEFVRFDSDAENPRYEPQVPWMEQEGPEYWERITQVAKGQEQWFRVNLRTLLGYYNQSAGGTHTLQRMYGCDVGSDGRLLRGYEQFAYDGCDYIALNEDLRTWTAADMAAQITRRKWEQAGAAEYYRAYLEGECVEWLHRYLKNG',
            'TCRA':'AQSVTQPDARVTVSEGASLQLRCKYSYSATPYLFWYVQYPRQGLQMLLKYYSGDPVVQGVNGFEAEFSKSDSSFHLRKASVHWSDSAVYFCAVSAKGTGSKLSFGKGAKLTVSPNIQNPDPAVYQLRDSK',
            'TCRB':'AAVTQSPRNKVTVTGGNVTLSCRQTNSHNYMYWYRQDTGHGLRLIHYSYGAGNLQIGDVPDGYKATRTTQEDFFLLLELASPSQTSLYFCASSDAPGQLYFGEGSKLTVLEDLKNVFPPEVAVFEPSEAEISHTQKATLVCLATGFYPDHVELSWWVNGKEVHSGVCTDPQPLKEQPALNDSRYALSSRLRVSATFWQNPRNHFRCQVQFYGLSENDEWTQDRAKPVTQIVSAEAWGRA'
            }

    pdb_seqs = _get_sequences_from_pdb_files(pdb_files)

    for region,seq in homology_dict.items():
        for pdb,pdb_seqs in pdb_seqs.items():
            print 'PDB:',pdb
            for pdb_seq in pdb_seqs:
                alignments = pairwise2.align.globalxx(seq,pdb_seq)
                print max([hamming_dist(a[0],a[1]) for a in alignments])
            raw_input()
