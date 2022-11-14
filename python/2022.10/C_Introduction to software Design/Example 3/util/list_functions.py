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
    