#runs for Python 2.7

d = {"word1": "document1",
     "word2": "document1",
     "word3": "document2",
     "word4": "document1"}



def get_inverse_dictionary(d):
    inverse_d = {}
    for key, value in d.iteritems():
        if inverse_d.has_key(value):
            inverse_d[value].append(key)
        else:
            inverse_d[value] = [key]
    for key, value in inverse_d.iteritems():
        inverse_d[key] = sorted(inverse_d[key])
    return inverse_d

inverse_d = get_inverse_dictionary(d)
assert(inverse_d == {"document1": ["word1", "word2", "word4"],"document2": ["word3"]})
print(inverse_d)