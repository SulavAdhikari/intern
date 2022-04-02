dict1 = {
    'name':'sulav adhikari',
    'age':16,
    'isGraduated': False
}

schema = {
    'name':{'type':'string',"min":0, 'max':20},
    'age':{'type':'integer','min':10, 'max':30},
    'isGraduated':{'type':'boolean', 'value':False},
}

def validate(dict, schema):
    list_of_dict = dict.items()
    list_of_schema = schema.items()
    

    for tuple in list_of_schema:
        if tuple[0] not in dict:
            return False

    for tuple in list_of_dict:

        
        if schema[tuple[0]]:
            value = schema[tuple[0]]

            if value['type'] == 'string':
                if not isinstance(tuple[1], str):
                    return False
                if len(tuple[1]) < value['min'] or len(tuple[1]) > value['max']:
                    return False
            if value['type'] == 'integer':
                if not isinstance(tuple[1], int):
                    return False
                if tuple[1] < value['min'] or tuple[1] > value['max']:
                    return False
            if value['type'] == 'boolean':
                if not isinstance(tuple[1], bool):
                    return False
                if tuple[1] != value['value']:
                    return False
    return True

print(validate(dict1, schema))      
