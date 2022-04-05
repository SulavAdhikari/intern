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
    dict_keys = list(dict.keys())
    schema_keys = list(schema.keys())

    # dict_values = dict.values()
    # schema_values = schema.values
    c = 0
    for key in schema_keys:
        
        if key in dict:
            dict_value = dict[key]
            schema_value = schema[key]
            if schema_value['type'] == 'string':
                if not isinstance(dict_value, str):
                    return False
                if len(dict_value) < schema_value['min'] or len(dict_value) > schema_value['max']:
                    return False
            if schema_value['type'] == 'integer':
                if not isinstance(dict_value, int):
                    return False
                if dict_value > schema_value['max'] or dict_value< schema_value['min']:
                    return False
            if schema_value['type'] == 'boolean':
                if not isinstance(dict_value, bool):
                    return False
                if dict_value != schema_value['value']:
                    return False

        if key not in dict_keys:
            return False
    return True

print(validate(dict1, schema))      
