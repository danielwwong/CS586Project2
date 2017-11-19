import pickle
import json
import os

file_des = os.path.join(os.path.dirname(__file__) , '8000000_80126615.pkl')
output_des = os.path.join(os.path.dirname(__file__) , 'output.json')

read = []

with open(file_des, "rb") as src:
    while 1:
        try:
            read.append(pickle.load(src))
        except EOFError:
            break

with open(output_des, 'w') as o:
    json.dump(read, o)
o.close()

#print (read[39]['@ID'])
#print (len(read[39]['TrackDetail']))
#for i in range(0, len(read[39]['TrackDetail'])):
#    print (read[39]['TrackDetail'][i]['EventTime'])
#    print (read[39]['TrackDetail'][i]['EventDate'])
#    print (read[39]['TrackDetail'][i]['Event'])
#    print (read[39]['TrackDetail'][i]['EventZIPCode'])
