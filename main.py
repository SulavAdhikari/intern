

# first lets take the part of rules as variables and also the dict
def is_valid(dict, max_len,min_len,max_val,min_val,boolval):
    #get the dict as list of tuples
    values = dict.items()
    #every field in dict is now a tuple 
    #
    for value in values:
        if isinstance(value[1], str):
            if len(value[1])>max_len or len(value[1])<min_len:
                return False
        if isinstance(value[1], int):
            if value[1]>max_val or value[1]<min_val:
                return False
        if isinstance(value[1], bool):
            if boolval != value[1]:
                return False
    return True



