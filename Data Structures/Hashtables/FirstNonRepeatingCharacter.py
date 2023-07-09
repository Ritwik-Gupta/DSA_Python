def first_non_repeating_char(string):
    myDict = {}
    for i in string:
        if i not in myDict:
            myDict[i] = True
        else:
            myDict[i] = False
            
    for i in string:
        if myDict[i]:
            return i
    
    return None



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""