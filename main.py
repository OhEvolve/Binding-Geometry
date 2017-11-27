
"""
Main function for testing
"""

# standard libraries

# nonstandard libraries

# homegrown libraries
from methods import import_data


# main function

def main():

    data_fname = 'pMHC-TCR-structures.csv'

    import_data.import_data(data_fname)



if __name__ == '__main__':
    main()
