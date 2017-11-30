import os
import json
import pandas as pd

lat = []
lon = []
flag = 0

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'dev-geo.json')) as src:
    coordinate = json.load(src)

count = len(coordinate)#41081

data = pd.read_csv(os.path.join(__location__, 'source_ctn.csv'), dtype = str)
data.head()

zip = data['source']
countZip = len(zip)

for i in range(0, countZip):
    for j in range(0, count):
        if coordinate[j]['city_zip'] == zip[i]:
            lat.append(coordinate[j]['city_lat'])
            lon.append(coordinate[j]['city_lon'])
            flag = 1
    if flag == 0:
        lat.append('none')
        lon.append('none')
        flag = 1
    flag = 0

with open(os.path.join(__location__, 'output.csv'), 'w') as output:
    output.write('lat,lon\n')
    for i in range(0, countZip):
        output.write(str(lat[i]))
        output.write(',')
        output.write(str(lon[i]))
        output.write('\n')
