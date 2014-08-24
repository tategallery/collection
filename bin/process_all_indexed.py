'''
	Go through all artwork jsons and produce an index for
	level0, level1, level2 while noting the relationships
	between the levels: parent0 (level0) and parent1 (level1)

	Outputs a json array
'''

import json
from os import walk

# use dict to elimiate duplicated entries as new entries
# are added as {'value of id': 'value of name'}
ids = []
level0list = []
level1list = []
level2list = []

def open_files(targetpath):
	for dirname, dirnames, filenames in walk(targetpath):

		for filename in filenames:

			filepath = '/'.join([dirname,filename])
			fileopen = open(filepath).read().decode('utf-8')
			jsonopen = json.loads(fileopen)

			get_all_subjects(jsonopen)

def get_all_subjects(jsonfile):
	subjectcount = jsonfile['subjectCount']

	if subjectcount is not 0:
		subjects0 = jsonfile['subjects']['children']

		for child0 in subjects0:
			subjects1 = child0['children']
			process_child(child0,'none','none',level0list)

		for child1 in subjects1:
			subjects2 = child1['children']
			process_child(child1,'none',child0['id'],level1list)

		for child2 in subjects2:
			process_child(child2,child1['id'],child0['id'],level2list)

def process_child(child, parent1,parent0,levellist):
	item = {}
	if child['id'] not in ids:
		item['id'] = child['id']
		item['name'] = child['name']
		item['parent1'] = parent1
		item['parent0'] = parent0
		ids.append(child['id'])
		levellist.append(item)

def write_files(data, filename):
	jsondata = json.dumps(data,sort_keys = True,separators = (',',':'))
	output = open('../processed/' + filename,'w')
	output.writelines(jsondata)
	output.close()

open_files('../artworks')

write_files(level0list,'level0list.json')
write_files(level1list,'level1list.json')
write_files(level2list,'level2list.json')
