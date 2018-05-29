# Dictionaries ZIP #

A = dict(zip('abcdef', list(range(6))))
for key, val in A.items():
    print(key, val)

####SORT BY KEY AND DICT GET AND ITEMS####
for word in wordlist:
    v = d.get(word, 0)
    v += 1
    d[word] = v

orderbykey = list(d.items())
orderbykey.sort(key = lambda x: (-x[1], x[0]))
