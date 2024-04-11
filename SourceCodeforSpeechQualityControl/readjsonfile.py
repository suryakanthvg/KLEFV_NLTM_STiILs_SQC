# Python program to read
# json file
import json
import time
# Opening JSON file
f = open('bn_IN_9440434_20221203_Right.json')

# returns JSON object as
# a dictionary
data = json.load(f)
# Iterating through the json
# list
for i in data['segments']:
    print(i)
    time.sleep(2)

    print(i["transcription"])
    print("")
    # for j in i:
    #   print(i[j])
    #   time.sleep(2)

# Closing file
f.close()

