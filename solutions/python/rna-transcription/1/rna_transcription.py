"""RNA complement of a given DNA sequence.
"""
def to_rna(dna_strand):
    """    G -> C
            C -> G
            T -> A
            A -> U
            """
    pares={"G":"C","C":"G","T":"A","A":"U"}
    rna_strand=""
    for character in dna_strand:
        rna_strand+=pares[character]
        
    return rna_strand