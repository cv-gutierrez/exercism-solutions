""" Diamond kata
"""
def rows(letter):
    """Dummy comment
    """
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index=alphabet.find(letter)
    top=[]
    bottom=[]
    space=" "
    
    for id in range(0,index+1,1):
        if id==0:
            row=space*(index -id) + alphabet[id]+space*(index-id)
        else:
            row=space*(index -id)+alphabet[id]+space*(2*id-1)+alphabet[id]+space*(index-id)
        top.append(row) 
        if id<index:
            bottom.append(row)
    bottom.reverse()
    top.extend(bottom)
    return top