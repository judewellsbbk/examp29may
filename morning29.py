astring = 'abcdefg'
nums = list(range(7))
d = dict(zip(astring, nums))
##
##for blah in d:
##    print(blah, d[blah])
##    
##print(d)

astring = 'this is a fairly simple this this simple what will we list string which has a bunch of words I\'m not sure what will happen when I make it into a list because it is a string right now perhaps I should be worried'

wordlist = astring.split()

for word in wordlist:
    v = d.get(word, 0)
    v += 1
    d[word] = v

orderbykey = list(d.items())
orderbykey.sort(key = lambda x: (-x[1], x[0]))


def multtwo(n):
    return n+n
# write a few more lines over here

a = [1,2,3,4,5,6]

print(list(filter(lambda e: e%2 ==0, a)))
