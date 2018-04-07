import json
import csv

# data = json.loads(open('/home/paulomoraes/Projects/blueway/back/dataset/apps.csv', 'r'))
o_file = open('/home/paulomoraes/Projects/blueway/back/dataset/apps_filters.csv', 'w')
# arr = data.read().strip().split()
data = []
with open('/home/paulomoraes/Projects/blueway/back/dataset/apps.csv') as doc:
    aux = csv.reader(doc, delimiter='}')
    i = 0
    for row in aux:
        app = ', '.join(row)
        i += 1
        data.append(app)
    print(i)
    #    print(', '.join(row))

# for row in data:
print(len(data))
