import os
import json
import pandas as pd

city = []
county = []
flag = 0

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'dev-geo.json')) as src:
    coordinate = json.load(src)

count = len(coordinate)#41081

data = pd.read_csv(os.path.join(__location__, 'over_source.csv'), dtype = str)
data.head()

zip = data['Source']
countZip = len(zip)

for i in range(0, countZip):
    for j in range(0, count):
        if coordinate[j]['city_zip'] == zip[i]:
            city.append(coordinate[j]['city_name'])
            county.append(coordinate[j]['city_county'])
            flag = 1
    if flag == 0:
        city.append('none')
        county.append('none')
        flag = 1
    flag = 0

with open(os.path.join(__location__, 'output.csv'), 'w') as output:
    output.write('city,county\n')
    for i in range(0, countZip):
        output.write(str(city[i]))
        output.write(',')
        output.write(str(county[i]))
        output.write('\n')
