'''
	Loads one json file and parse the 'subjects' field from a nested
	structure to a flat one. id/name hierarhcy is indexed, eg:

	id0 - grandparernt
	id1 - parent
	id2 - child

	thingList(list) will be populated, and turned into json array
	thing(dict) is associated with each child node
'''

import json

sample = json.loads(open('artworks/a/000/a00001-1035.json').read().decode('utf-8'))
subjects = sample['subjects']

thingList = []

def get_child(children,i):
	for child in children:
		thing = {}
		thing['id_'+str(i)] = child.get('id')
		thing['name_'+str(i)] = child.get('name')
		thingList.append(thing)
		get_all_children(child,i + 1)

def get_all_children(subjects,i):
	if type(subjects) is dict:
		children = subjects.get('children')
		if children is not None:
			get_child(children,i)
		else:
			print 'Reached the end'
	elif type(subjects) is list:
		children = subjects
		get_child(children,i)

get_all_children(subjects,0)

jsondata = json.dumps(thingList, sort_keys = True, separators = (',',':'))

output = open('processed/processed_one.json','w')
output.writelines(jsondata)
output.close()
