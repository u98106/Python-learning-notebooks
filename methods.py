#!/usr/bin/python

import ipy_table as ipt

''' f: member name as str
'''
def isMethod(f):
    return not (f.startswith('_') or f.endswith('_'))


''' Splits a list into 'nelems' elements
    Returns a list-of-lists (lol :)
    '''
def l2ll(objs, nelems=3):
    lol = []
    for i in range(0,len(objs), nelems):
        lol.append(objs[i:i+nelems])

    # pad last 'incomplete row' to 'nelems'
    deficit = nelems - len(lol[-1])
    lol[-1].extend(['']*deficit)

    return lol


def methods(obj):
    d = dir(obj)
    d = filter(isMethod, d)
    return ipt.make_table(l2ll(d))



if __name__ == '__main__':
    print 'Running tests...'
    print int
    print methods(int)
    print str
    print methods(str)
    print list
    print methods(list)
    obj = (1,2,3)
    print obj
    print methods(obj)
