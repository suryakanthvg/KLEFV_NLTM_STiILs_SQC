import json
# Writing to sample.json
#using dumps
with open("generated_sample.json", "w") as outfile:
    # Data to be written
    n1 = "Suryakanth"
    dictionary = {"name": n1, "rollno": 56, "cgpa": 8.6, "phonenumber": "9976770500" }
# Serializing json
#    json.dump(dictionary,outfile)
    json_object = json.dumps(dictionary, indent=8)
    outfile.write(json_object)
    outfile.write(",")
    n1 = "Chandrakanth"
    dictionary = {"name": n1, "rollno": 56, "cgpa": 8.6, "phonenumber": "9976770500" }
# Serializing json
    json_object = json.dumps(dictionary, indent=8)
    outfile.write(json_object)
    outfile.write(",")
    n1 = "Ramesh"
    dictionary = {"name": n1, "rollno": 56, "cgpa": 8.6, "phonenumber": "9976770500" }
# Serializing json
    json_object = json.dumps(dictionary, indent=8)
    outfile.write(json_object)
    outfile.write(",")



#using dumps

