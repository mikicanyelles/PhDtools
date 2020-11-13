
def dna_to_prot(dna_seq, direction='both', frame=0, codification=1):
    '''
    DESCRIPTION:
        This function converts a DNA sequence into an aminoacidic sequence.

    INPUTS:
        - seq           --> sequence to translate
        - direction     --> sets the direction of encoding
                        --> Options:
                            --> 'both': returns both the forward and reverse translations
                            --> 'forward', 'f', '53', 53: returns the forward translation
                            --> 'reverse', 'r', '35', 35: returns the reverse translation
        - frame         --> sets the starting frame for the translation
                        --> Options:
                            --> 0: returns the translation starting from all the frames (1, 2 and 3)
                            --> 1: returns the translation statring from the first frame
                            --> 2: returns the translation statring from the second frame
                            --> 3: returns the translation statring from the third frame
        - codification  --> sets the style of aminoacids codification
                        --> Options:
                            --> 1: returns the 1-letter code of the aminoacids
                            --> 3: returns the 3-letter code of the aminoacids
    '''

    translation_1_letter = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

    dna_seq = dna_seq.upper()

    if '\n' in dna_seq:
        dna_seq = dna_seq.replace('\n', '')


    for i in range(len(dna_seq)):
        if dna_seq[i] not in ('A', 'C', 'G', 'T'):
            raise 'NotDNASequenceError'


    def translator(dna_seq, frame, translation_table=translation_1_letter):
        frame = frame-1

        protein_seq = ''

        for i in range(frame,len(dna_seq[frame:]), 3):
            try:
                dna_seq[i+3]
                codon = dna_seq[i:i+3]
                protein_seq += translation_table[codon]
            except IndexError:
                pass

        return protein_seq

    protein_seq = dict()
    if direction == 'both':
        #forward
        if frame == 0:
            for f in (1,2,3):
                if codification == 1:
                    protein_seq['forward', 'frame %s' % f] = translator(dna_seq, f, translation_1_letter)

        elif frame in (1,2,3):
            if codification == 1:
                protein_seq['forward', 'frame %s' % f] = translator(dna_seq, f, translation_1_letter)

        #reverse
        if frame == 0:
            for f in (1,2,3):
                if codification == 1:
                    protein_seq['forward', 'frame %s' % f] = translator(dna_seq[::-1], f, translation_1_letter)

        elif frame in (1,2,3):
            if codification == 1:
                protein_seq['forward', 'frame %s' % f] = translator(dna_seq[::-1], f, translation_1_letter)


    elif direction in ('forward', 'f', '53', 53):
        #forward
        if frame == 0:
            for f in (1,2,3):
                if codification == 1:
                    protein_seq['forward', 'frame %s' % f] = translator(dna_seq, f, translation_1_letter)

        elif frame in (1,2,3):
            if codification == 1:
                protein_seq['forward', 'frame %s' % f] = translator(dna_seq, f, translation_1_letter)

    elif direction in ('reverse', 'r', '35', 35):
        #reverse
        if frame == 0:
            for f in (1,2,3):
                if codification == 1:
                    protein_seq['reverse', 'frame %s' % f] = translator(dna_seq[::-1], f, translation_1_letter)

        elif frame in (1,2,3):
            if codification == 1:
                protein_seq['reverse', 'frame %s' % f] = translator(dna_seq[::-1], f, translation_1_letter)

    return protein_seq


