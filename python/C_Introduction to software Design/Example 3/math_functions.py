"""
LIST FUNCTIONS
"""

def get_max(lst):
    mx = float('-inf')
    
    for num in lst:
        if num > mx:
            mx = num
        
    return mx

def get_min(lst):
    mn = float('inf')
    
    for num in lst:
        if num < mn:
            mn = num
    
    return mn

def get_average(lst):
    return sum(lst) / len(lst)

def get_median(lst):
    lst = sorted(lst)
    
    if len(lst) % 2 == 0:
        return(lst[(len(lst) / 2) - 1] + lst[(len(lst) / 2)]) / 2
    else:
        return lst[(len(lst) - 1) / 2]
    
"""
HASH TABLE FUNCTIONS
"""

def get_keys(ht):
    return ht.keys()

def has_key(ht, key):
    return key in ht

def get_max(ht):
    """
    assume all values are int
    """
    mx = float('-inf')
    for k, v in ht.items():
        if v > mx:
            mx = v
            
        return mx
    
def get_min(ht):
    """
    assume all values are int
    """
    mn = float('-inf')
    for k, v in ht.items():
        if v < mn:
            mn = v
            
        return mn