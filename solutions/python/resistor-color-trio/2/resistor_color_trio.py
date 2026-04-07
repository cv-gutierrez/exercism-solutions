""" Color code for resistors
"""

def label(colors):
    """ Dummy comment
    """
    result=str(color_code(colors[0]))
    if result=="0":
        result=""
    code=int(color_code(colors[2]))
    
    if color_code(colors[1])==0:
        code+=1
    else:
        result+=str(color_code(colors[1]))
    zeros=10**code
    #if zeros grater than 9 then add giga
    if code>=9:
        giga_number=str(zeros)[:-9]
        return str(result) +giga_number[1:]+" gigaohms"

    #if zeros grater than 6 then add mega
    if code>=6:
        mega_number=str(zeros)[:-6]
        return str(result) +mega_number[1:]+" megaohms"

    #if zeros are grater than 3 then add Kilo
    if code>=3:
        kilo_number=str(zeros)[:-3]
        return result +kilo_number[1:]+" kiloohms"
    return result+str(zeros)[1:]+" ohms"
  
def color_code(color):
    """Function to return de int number based on label string
    """
    if color=="black":
        return 0
    if color=="brown":
        return 1
    if color=="red":
        return 2
    if color=="orange":
        return 3
    if color==  "yellow":
        return 4
    if color=="green":
        return 5
    if color=="blue":
        return 6
    if color=="violet":
        return 7
    if color=="grey":
        return 8
    if color=="white":
        return 9
    return -1