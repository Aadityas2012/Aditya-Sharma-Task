#In Challenge 1 we set up environment.
#In Challenge 2 we extract the meta data in json format.
#Now in Challange 3 we are going to read the json data.

#Our json file is my_data
#If we want to get the value of the first key, then-

import json
with open("my_data.json") as f:
	data = json.load(f)
my_value = data["key1"]["value1"]
print(my_value)

#Here we import the json module, this will allow you to transform the data into a python dictionary via the json.load() function.
#If there are multiple values in the key we can access it by indexing e.g. for first value index is 0

import json
with open("my_data.json") as f:
	data = json.load(f)
my_value = data["key1"]["key2"][0]["value1"]
print(my_value)

#If we want to get all the values then we will use for loop

import json
with open("my_data.json") as f:
	data = json.load(f)
my_list = []
my_key1 = data["key1"]
for i in my_key1:
	my_key2 = i["key2]
	for j in my_key2:
		my_value = j["value1"]
		my_list.append(my_value)
print(my_list)

#If some of the key is missing i.e. KeyError
#Add a default value with get() function

import json
with open("my_data.json") as f:
	data = json.load(f)
my_list = []
my_key1 = data["key1"]
for i in my_key1:
	my_key2 = i["key2]
	for j in my_key2:
		my_value = j.get("value1", "NotAvailable")
		my_list.append(my_value)
print(my_list)