import numpy as np
from pqdict import pqdict


def mins(df):
    '''
    Function for exploring a bidimensional PES in order to find minima in the surface.
    '''

    lims = list(df.shape) #shape is a tuple containing the (y,x) shape

    mins = dict()
    for x in range(lims[0]):
        for y in range(lims[1]):
            is_min = []
            if str(df.iloc[x][y]) != 'nan': #this avoid failures in uncomplete PESs
                try :
                    is_min.append(df.iloc[x][y] < df.iloc[x-1][y-1])
                except (ValueError, IndexError, KeyError):
                    pass

                try :
                    is_min.append(df.iloc[x][y] < df.iloc[x][y-1])
                except (ValueError, IndexError, KeyError):
                    pass

                try :
                    is_min.append(df.iloc[x][y] < df.iloc[x+1][y-1])
                except (ValueError, IndexError, KeyError):
                    pass

                try :
                    is_min.append(df.iloc[x][y] < df.iloc[x-1][y])
                except (ValueError, IndexError, KeyError):
                    pass

                try :
                    is_min.append(df.iloc[x][y] < df.iloc[x+1][y])
                except (ValueError, IndexError, KeyError):
                    pass

                try :
                    is_min.append(df.iloc[x][y] < df.iloc[x-1][y+1])
                except (ValueError, IndexError, KeyError):
                    pass

                try :
                    is_min.append(df.iloc[x][y] < df.iloc[x][y+1])
                except (ValueError, IndexError, KeyError):
                    pass

                try :
                    is_min.append(df.iloc[x][y] < df.iloc[x+1][y+1])
                except (ValueError, IndexError, KeyError):
                    pass

            if False not in is_min:
                mins[(x,y)] = round(df.iloc[x][y], 2)

    return mins


def path(pes, starting_point, ending_point):
    '''
    Dijsktra algorithm applied to the search of lowest-energy paths between two pre-selected points in a 2D PES.
    It is an adaptation of the BBSysDyn's version uploaded to https://math.stackexchange.com/questions/3088292/finding-lowest-elevation-path-between-two-points
    '''

    def get_neighbor_idx(x,y,dims):
        res = []
        for i in ([0,-1,1]):
            for j in ([0,-1,1]):
                if i==0 and j==0: continue
                if x+i<(dims[0]) and x+i>-1 and y+j<(dims[1]) and y+j>-1:
                    res.append((x+i,y+j))
        return res

    D = {}
    P = {}
    Q = pqdict()
    Q[starting_point] = 0

    while len(Q)>0:
        (v,vv) = Q.popitem()
        D[v] = vv
        neighs = get_neighbor_idx(v[0],v[1],pes.shape)
        for w in neighs:
            vwLength = D[v] + np.abs(pes[v[0],v[1]] - pes[w[0],w[1]])
            if w in D:
                if vwLength < D[v]:
                    raise ValueError
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    path = []
    while 1:
       path.append(ending_point)
       if ending_point == starting_point: break
       ending_point = P[ending_point]
    path.reverse()

    return path


def stationary_points(path_energies):
    '''
    Function for outputing a dict with all the stationary points found in a given path.
    dict will contain the points as keys and a list of type of structure and energy
    '''

    stationary_points = dict()

    TSs = 0; MINs = 0
    for i in range(len(path_energies)):

        if i not in (0, len(path_energies) -1):
            if list(path_energies.values())[i] < list(path_energies.values())[i-1] and list(path_energies.values())[i] < list(path_energies.values())[i+1]:
                stationary_points[list(path_energies.keys())[i]] = ['min', list(path_energies.values())[i]]
                MINs += 1

            if list(path_energies.values())[i] > list(path_energies.values())[i-1] and list(path_energies.values())[i] > list(path_energies.values())[i+1]:
                stationary_points[list(path_energies.keys())[i]] = ['TS', list(path_energies.values())[i]]
                TSs += 1

        elif i == 0:
            if list(path_energies.values())[i] < list(path_energies.values())[i+1]:
                stationary_points[list(path_energies.keys())[i]] = ['min', list(path_energies.values())[i]]
                MINs += 1

        elif i == (len(path_energies) -1):
            if list(path_energies.values())[i] < list(path_energies.values())[i-1]:
                stationary_points[list(path_energies.keys())[i]] = ['min', list(path_energies.values())[i]]
                MINs += 1

    TS = 0; INT = 0

    for i in range(len(stationary_points)):
        if i == 0:
            stationary_points[list(stationary_points.keys())[i]][0] = 'RC'

        elif i != 0 and i != (len(stationary_points) -1):
            if list(stationary_points.values())[i][0] == 'TS':
                if TS > 1:
                    TS +=1
                    stationary_points[list(stationary_points.keys())[i]][0] = 'TS%s' % TS
                if TS == 1:
                    stationary_points[list(stationary_points.keys())[i]][0] = 'TS'

            if list(stationary_points.values())[i][0] == 'min':
                if MINs > 2:
                    stationary_points[list(stationary_points.keys())[i]][0] = 'INT%s' % INT
                    INT +=1
                elif MINs == 2:
                    stationary_points[list(stationary_points.keys())[i]][0] = 'PD'

        elif i == (len(stationary_points) -1):
            stationary_points[list(stationary_points.keys())[i]][0] = 'PD'


    return stationary_points

