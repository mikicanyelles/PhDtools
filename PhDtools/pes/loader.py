from pandas import DataFrame, read_csv
from numpy import array

def load_PES_from_2d_csv(filename):
    '''
    Function for loading a 2D PES from a csv file containing all the energys in a bidimensional matrix
    '''

    pes_pd = DataFrame(read_csv(filename))
    pes_np = array(pes_pd)


    return pes_np, pes_pd
