# Python program to read
# json file
import json
import time
# Opening JSON file
f = open('samplejsonfile.json')

# returns JSON object as
# a dictionary
data = json.load(f)
# Iterating through the json
# list
for i in data['faculty']:
    print(i)
    print("")
    time.sleep(2)

    print(i["fareaofr"])
    print("")
    time.sleep(2)
    # for j in i:
    #   print(i[j])
    #   time.sleep(2)

for j in data['student']:
    print(j)
    print("")
    time.sleep(2)

    print(j["sareaofr"])
    print("")
    time.sleep(2)
# Closing file
f.close()

