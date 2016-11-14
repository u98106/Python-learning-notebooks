#!/usr/bin/python


filename = 'sales1.csv'
f = open(filename)


books = {}
f.readline()
for line in f:
    title, numsold, saleprice, royalty = line.strip().split(',')
    books[title] = [int(numsold), float(saleprice), float(royalty)]

#from pprint import pprint
#pprint(books)

while True:
    title = raw_input('Enter title: ')
    if title in books:
        print books[title]
    else:
        print 'Title not found!'







