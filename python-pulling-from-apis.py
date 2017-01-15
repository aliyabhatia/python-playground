# Making something that pulls from the FEC's data

import requests # this is a very simple http requests plugin
from pprint import pprint # imports pprint

# below is just some sample ways to use requests

# r = requests.get("http://httpbin.org/ip") 

# print(r) # the whole object
# print(r.headers) # gives you the response headers
# print(r.encoding) # not that useful
# print(r.text) # gives you response but as a string
# print(type(r.text)) # should give you unicode string
# print(r.json()) # gives you the JSON version in a python dictionary
# print(type(r.json())) # should give you dict aka a dictionary

# r = requests.get("https://api.open.fec.gov/v1/candidates/?api_key=DEMO_KEY&candidate_status=C&federal_funds_flag=true&sort_hide_null=true&sort=name&page=1&per_page=20")
# # print(r)

# jsondata = r.json()
# # pprint(jsondata[0]) # this didn't work because this was not a list object - so paste URL and see structure and then re-design your code appropriately
# # what you find is there is some extra data besides the candidates
# candidateslist =jsondata["results"] # storing candidate data to a new list variable - remember most keys will be strings!
# pprint(candidateslist[0])

candidates = []
pagenum = 1

# capture all the data by hitting the api

while True:
	url =  "https://api.open.fec.gov/v1/candidates/?api_key=DEMO_KEY&candidate_status=C&federal_funds_flag=true&sort_hide_null=true&sort=name&page=" + str(pagenum) + "&per_page=20"
	response = requests.get(url)
	jsondata = response.json()
	results = jsondata["results"]
	if results == []:
		break
	candidates = candidates + results # this works when you are adding 2 lists together but wouldn't work if you were adding a string to a list
	pagenum += 1

print(len(candidates))


# loop through candidates and collect their names

candidatenames = []

for candidate in candidates:
	candidatenames.append(candidate["name"])

pprint(candidatenames)

# loop through candidates and create JSON that will be useful to you
# usually that will involve hitting more than one endpoint but here it was just one 

candidatedata = []

for candidate in candidates:
	name = candidate["name"]
	candidate_id = candidate["candidate_id"]
	# if you wanted to pull another variable from the FEC API, e.g. money, you would do that here
	# using the candidate id
	# then use the rest of this to put all of that in one list of dictionaries
	item = {
		"name":name,
		"candidate_id":candidate_id,
		"money":10
	}
	candidatedata.append(item)

pprint(candidatedata)


