sentences = ['The fox had two tails.', 'The sky is pinker than yesterday.','We are searching for tomorrow.']
punc = """!()-[]{;}:'"\,<>./?@#$%^&*_~"""
dict_var = {} 
c = 0 
for sentence in sentences:
    for ele in punc:
        if ele in sentence:
            sentence.replace(ele, '')
    words = sentence.split(' ')
    for word in words:
        if word in list(dict_var.keys()):
            dict_var[word].append(c)
        if word not in list(dict_var.keys()):
            dict_var[word] = list()
            dict_var[word].append(c)
    c +=1

def search(keyword):
    if keyword in list(dict_var.keys()):
        indexes = dict_var[keyword]
        return indexes
    return None

print(search('The'))