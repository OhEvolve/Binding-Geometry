
"""
Main function for testing
"""

# standard libraries

# nonstandard libraries

# homegrown libraries
from methods import import_data
from methods import overview_data


# main function

def main():

    data_fname = 'pMHC-TCR-structures.csv'

    data = import_data.import_data(data_fname)
    #overview_data.chain_length_frequency(data)
    overview_data.alignment(data)



if __name__ == '__main__':
    main()
