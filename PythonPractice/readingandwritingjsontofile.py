import json
# Python program to read from one json file and write into another json file
import time
# Opening JSON file
f = open('bn_IN_9440434_20221203_Right.json')
# returns JSON object as a dictionary
data = json.load(f)

# Writing to generated_bn_IN_9440434_20221203_Right.json
#using dumps
with open("generated_bn_IN_9440434_20221203_Right.json", "w") as outfile:
    # Data to be written

    initialmetadata = '''
    {
    "domain" : "Telecom",
    "topic" : "Customer reviews",
    "language" : "bn_IN",
    "speechDuration" : 554.22,
    "audioDuration" : 1130.0,
    '''
    metadata = json.loads(initialmetadata)
    json_object = json.dumps(metadata, indent=8)
    outfile.write(json_object)

    for i in data['segments']:
#    for i in data['speakers']:
# Serializing json
#       transcriptionscript=json_encode(i["tranascription"], JSON_UNESCAPED_UNICODE)
#       i["tranascription"]=transcriptionscript
       json_object = json.dumps(i, indent=8)
       outfile.write(json_object)
#       outfile.write(",")



