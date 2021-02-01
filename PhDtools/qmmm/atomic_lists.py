'''
Package for leading with the creation and modification of a atomic lists for ChemShell specifications.
'''


def residue_selecter(residue_index, pdb, backbone=False, custom_resids=[]):
    '''
    Function for creating a list of atoms selected by their residue index.
    By default it unselects backbone atoms (this can be deactivated by setting backbone=True).

    In order to check which are standard residues (so backbone is present), a list has been created
    (which will be made accessible). Other custom names (like the ones created by MCPB, f.e) for
    standard residues can be added by the user by passing through a list of them with the argument
    'custom_resids'.
    '''

    from MDAnalysis import Universe

    # standard residues
    std_resids = ['ACE', 'ALA', 'ALAD', 'ARG', 'ARGN', 'ASF', 'ASH', 'ASN', 'ASN1',
                'ASP', 'ASPH', 'CALA', 'CARG', 'CASF', 'CASN', 'CASP', 'CCYS', 'CCYX',
                'CGLN', 'CGLU', 'CGLY', 'CHID', 'CHIE', 'CHIP', 'CILE', 'CLEU', 'CLYS',
                'CME', 'CMET', 'CPHE', 'CPRO', 'CSER', 'CTHR', 'CTRP', 'CTYR', 'CVAL',
                'CYM', 'CYS', 'CYS1', 'CYS2', 'CYSH', 'CYX', 'DAB', 'GLH', 'GLN', 'GLU',
                'GLUH', 'GLY', 'HID', 'HIE', 'HIP', 'HIS', 'HIS1', 'HIS2', 'HISA', 'HISB',
                'HISD', 'HISE', 'HISH', 'HSD', 'HSE', 'HSP', 'HYP', 'ILE', 'LEU', 'LYN',
                'LYS', 'LYSH', 'MET', 'MSE', 'NALA', 'NARG', 'NASN', 'NASP', 'NCYS', 'NCYX',
                'NGLN', 'NGLU', 'NGLY', 'NHID', 'NHIE', 'NHIP', 'NILE', 'NLEU', 'NLYS', 'NME',
                'NMET', 'NPHE', 'NPRO', 'NSER', 'NTHR', 'NTRP', 'NTYR', 'NVAL', 'ORN', 'PGLU',
                'PHE', 'PRO', 'QLN', 'SER', 'THR', 'TRP', 'TYR', 'VAL']


    std_resids += custom_resids

    atom_list = []
    u = Universe(pdb)

    for res in residue_index:
        sel = u.select_atoms('resid %s' % res)

        if str(sel.residues).split(' ')[2][:-1] in std_resids:
            if backbone:
                sel = u.select_atoms('resid %s and not (name O or name C or name CA or name H or name HA or name N)' % res)

        else :
            sel = u.select_atoms('resid %s' % res)

        for at in range(len(sel)):
            atom_list.append(str(sel[at]).split(' ')[1][:-1])


    return atom_list



def list_creator(selection, old_list_file='', tcl_var='list'):
    '''
    Function for creating a tcl list specifying a list of atoms suitable for ChemShell.
    It can also append a new selection to an existing list inputed through the old_list
    parameter (inputed as the file route).
    It outputs the new list in tcl format ('set "tcl_var" { ... }', being
    tcl_var the given name for the list).
    '''

    new_list = []

    if old_list_file != '':
        old_list = open(old_list_file, 'r').read()
        old_list = old_list.replace('\n', '')
        old_list = old_list.replace('\\', '')
        old_list = old_list.split(' ')

        for at in old_list:
            try:
                new_list.append(int(at))
            except ValueError:
                pass

    for at in new_selection:
        try :
            new_list.append(int(at))
        except ValueError:
            pass

    if isinstance(new_selection[0], list):
        for lst in new_selection:
            for at in lst:
                try :
                    new_list.append(int(at))
                except ValueError:
                    pass

    new_list.sort()
    for at in range(len(new_list)):
        new_list[at] = str(new_list[at])

    print('The new list has %s atoms' % len(new_list))

    tcl_list_indexes = ' '.join(new_list)
    tcl_list = 'set %s { ' % tcl_var + tcl_list_indexes + '}'

    return tcl_list



