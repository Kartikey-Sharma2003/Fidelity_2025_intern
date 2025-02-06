from collections import defaultdict
def dv():
    return 'key is not found'
d1 = defaultdict(dv)
d1['a']=10
d1['b']=20
print(d1['c'])