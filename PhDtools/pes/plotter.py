import matplotlib.pyplot as plt
from .translator import points_to_coords


def bidimensional_pes(pes, x=None, y=None, plot_name=None, title=''):
    '''
    DESCRIPTION:
        Plots a contour map with the input info.
    '''


    if (x != None) and (y != None):
        plt.contour(x, y, pes, 7, cmap='nipy_spectral_r')
        plt.contourf(x, y, pes, 700, cmap='nipy_spectral', corner_mask=True)

    else :
        plt.contour(pes, 7, cmap='nipy_spectral_r')
        plt.contourf(pes, 700, cmap='nipy_spectral', corner_mask=True)

    plt.colorbar(ticks=range(0,61, 10), label='Energy (kcal/mol)')

    plt.xticks(range(-175,31,25))
    plt.xlabel('Rotation of C6-C7 (º)')
    plt.yticks(y)
    plt.ylabel('Epoxide Ring Opening (C6-O distance, Å)')
    #plt.zticks(range(0,60,10))
    if title != '':
        plt.title(title)

    if plot_name != None:
        plt.savefig(plot_name, dpi=300, transparent=False)
    plt.show()

def mins_in_2d_pes(pes, mins, x=None, y=None, plot_name='', title='', labels=['', '']):
    '''
    TODO:
        - [ ] consistent plot ticks
    DESCRIPTION:
        Plots a contour map labeling all the minima pipped as a dict.
    '''

    mins_points, mins_coords = points_to_coords(list(mins.keys()), y, x)

    if (x != None) and (y != None):
        plt.contour(x, y, pes, 7, cmap='nipy_spectral_r')
        plt.contourf(x, y, pes, 700, cmap='nipy_spectral', corner_mask=True)

    else :
        plt.contour(pes, 7, cmap='nipy_spectral_r')
        plt.contourf(pes, 700, cmap='nipy_spectral', corner_mask=True)

    plt.colorbar(ticks=range(0,61, 10), label='Energy (kcal/mol)')

    plt.scatter(mins_coords[1], mins_coords[0], color='white', zorder=1)


    bbox = dict(boxstyle='round,pad=0.2', fc='white')

    for i in range(len(mins_coords[0])):

        label = str(list(mins.values())[i])
        if i == 1:
            plt.annotate(label,
                        (mins_coords[1][i], mins_coords[0][i]),
                        textcoords='offset points',
                        xytext=(-20,0),
                        bbox= bbox,
                        ha='center')
        else :
            plt.annotate(label,
                    (mins_coords[1][i], mins_coords[0][i]),
                    textcoords='offset points',
                    xytext=(20,0),
                    bbox= bbox,
                    ha='center')

 #   plt.xticks(range(-175,31,25))
    if labels != ['','']:
        plt.xlabel(labels[0])#'Rotation of C6-C7 (º)')
        plt.ylabel(labels[1])#'Epoxide Ring Opening (C6-O distance, Å)')
    plt.yticks(y)
    #plt.ylabel('Epoxide Ring Opening (C6-O distance, Å)')
    #plt.zticks(range(0,60,10))
    if title != '':
        plt.title(title)

    if plot_name != None:
        plt.savefig(plot_name, dpi=300, transparent=False)
    plt.show()



def _mins_in_2d_pes(pes, mins, x=None, y=None, plot_name=None, title=''):
    '''
    DESCRIPTION:
        Plots a contour map labeling all the minima pipped as a dict.
    '''

    mins_points, mins_coords = points_to_coords(list(mins.keys()), y, x)

    if (x != None) and (y != None):
        plt.contour(x, y, pes, 7, cmap='nipy_spectral_r')
        plt.contourf(x, y, pes, 700, cmap='nipy_spectral', corner_mask=True)

    else :
        plt.contour(pes, 7, cmap='nipy_spectral_r')
        plt.contourf(pes, 700, cmap='nipy_spectral', corner_mask=True)

    plt.colorbar(ticks=range(0,61, 10), label='Energy (kcal/mol)')

    plt.scatter(mins_coords[1], mins_coords[0], color='white', zorder=1)


    bbox = dict(boxstyle='round,pad=0.2', fc='white')

    for i in range(len(mins_coords[0])):

        label = str(list(mins.values())[i])
        if i == 1:
            plt.annotate(label,
                        (mins_coords[1][i], mins_coords[0][i]),
                        textcoords='offset points',
                        xytext=(-20,0),
                        bbox= bbox,
                        ha='center')
        else :
            plt.annotate(label,
                    (mins_coords[1][i], mins_coords[0][i]),
                    textcoords='offset points',
                    xytext=(20,0),
                    bbox= bbox,
                    ha='center')

    plt.xticks(range(-175,31,25))
    plt.xlabel('Rotation of C6-C7 (º)')
    plt.yticks(y)
    plt.ylabel('Epoxide Ring Opening (C6-O distance, Å)')
    #plt.zticks(range(0,60,10))
    if title != '':
        plt.title(title)

    if plot_name != None:
        plt.savefig(plot_name, dpi=300, transparent=False)
    plt.show()
