# Calculate som-of-prods of two lists

#import pdb
#pdb.set_trace()

def sop(l1, l2):
    sum_ = 0
    c = []
    for i in range(len(l1)):
        c.append(l1[i]*l2[i])
    return sum(c)


def sop(l1, l2):
    sum_ = 0
    for n1, n2 in zip(l1, l2):
        sum_ += n1*n2
    return sum_






a = [1,2,3,4]
b = [0,-1,2,0]
ab = [[1,0], [2,-1], [3,2], [4,0]]

for pair in ab:
    sum += pair[0]*pair[1]



print sop(a,b)
