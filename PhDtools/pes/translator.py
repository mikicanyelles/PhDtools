
def points_to_coords(points_in, coords_rosetta1, coords_rosetta2):
    '''
    points has to be inputed as a list of 2-dimensional points ([x,y]).
    It will be returned a 2-dimensional list of lists containing a list with the x points and the list with the y points.
    The same with the coords output list. Both are suitable for plotting with
    '''

    points = [[],[]]
    coords = [[],[]]

    for i in range(len(points_in)):
        points[0].append(points_in[i][0])
        coords[0].append(coords_rosetta1[points_in[i][0]])

        points[1].append(points_in[i][1])
        coords[1].append(coords_rosetta2[points_in[i][1]])

    return points, coords


def path_energies(path, pes, decimals=2):
    '''
    Function for creating a dictionary with the energies of each point of a given path.
    pes has to be inputed as a DataFrame.
    '''

    energies = dict()
    for i in range(len(path)):
        energies[path[i]] = round(pes.iloc[path[i][0]][path[i][1]], decimals)

    return energies
