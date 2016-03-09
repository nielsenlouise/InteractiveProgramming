import csv
listlist = []
with open('test.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        listlist.append(row)
print listlist
