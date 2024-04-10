import json
people_string = '''
{
"people":[
{
  "emp_name": "John smith",
  "emp_no.": "924367-567-23",
  "emp_email": ["johnsmith@dummyemail.com"],
  "has_license": "false"
},
{
  "emp_name": "harshit kant",
  "emp_no.": "560-555-5153",
  "emp_email": "null",
  "has_license": "true"
}
]
}
'''
 
data = json.loads(people_string)
new_string = json.dumps(data, sort_keys=False, indent=3)
print(new_string)

