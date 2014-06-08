dnaF = open('rosalind_rna.txt')

for dna in dnaF:
    dna_lst = list(dna)
    for i in range(0,len(dna_lst)):
        if dna_lst[i] == 'T':
            dna_lst[i] = 'U'
    print("".join(dna_lst))
