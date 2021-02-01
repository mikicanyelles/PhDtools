from pandas import DataFrame, read_csv
from numpy import array

def load_PES_from_2d_csv(filename):
    '''
    Function for loading a 2D PES from a csv file containing all the energies in a bidimensional matrix (only the values, no labels nor titles)

    TODO:
        - [ ] Add possibility of using header or not and to specify columns and rows
    '''

    pes_pd = DataFrame(read_csv(filename, header=None))
    pes_np = array(pes_pd)


    return pes_np, pes_pd
