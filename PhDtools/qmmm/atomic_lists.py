from MDAnalysis import Universe

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



def list_appender(old_list, new_selection, tcl_var):
    '''
    Function for appending the new selection to the list. The new_selection 
    parameter can be both a list of integers or a list of lists of integers.
    It outputs the new list in tcl format ('set "tcl_var" { ... }', being 
    tcl_var the given name for the list).
    '''

    old_list = old_list.replace('\n', '')
    old_list = old_list.split(' ')

    new_list = []
    for at in old_list:
        try :
            int(at)
            new_list.append(at)
        except TypèError:
            pass

    if isinstance(new_selection[0], int):
        [new_list.append(at) for at in new_selection]
#        for at in new_selection:
#            new_list.append(at)

    elif isinstance(new_selection[0], list):
        [[new_list.append(at) for at in lst] for lst in new_selection]
#        for lst in new_selection:
#            for at in lst:
#                new_list.append(at)

    new_list.sort()


    tcl_list_indexes = ' '.join(new_list)
    tcl_list = 'set %s { ' % tcl_var + '}'



'ACE', 'ALA', 'ALAD', 'ARG', 'ARGN', 'ASF', 'ASH', 'ASN', 'ASN1', 'ASP', 'ASPH', 'CALA', 'CARG', 'CASF', 'CASN', 'CASP', 'CCYS', 'CCYX', 'CGLN', 'CGLU', 'CGLY', 'CHID', 'CHIE', 'CHIP', 'CILE', 'CLEU', 'CLYS', 'CME', 'CMET', 'CPHE', 'CPRO', 'CSER', 'CTHR', 'CTRP', 'CTYR', 'CVAL', 'CYM', 'CYS', 'CYS1', 'CYS2', 'CYSH', 'CYX', 'DAB', 'GLH', 'GLN', 'GLU', 'GLUH', 'GLY', 'HID', 'HIE', 'HIP', 'HIS', 'HIS1', 'HIS2', 'HISA', 'HISB', 'HISD', 'HISE', 'HISH', 'HSD', 'HSE', 'HSP', 'HYP', 'ILE', 'LEU', 'LYN', 'LYS', 'LYSH', 'MET', 'MSE', 'NALA', 'NARG', 'NASN', 'NASP', 'NCYS', 'NCYX', 'NGLN', 'NGLU', 'NGLY', 'NHID', 'NHIE', 'NHIP', 'NILE', 'NLEU', 'NLYS', 'NME', 'NMET', 'NPHE', 'NPRO', 'NSER', 'NTHR', 'NTRP', 'NTYR', 'NVAL', 'ORN', 'PGLU', 'PHE', 'PRO', 'QLN', 'SER', 'THR', 'TRP', 'TYR', 'VAL'
