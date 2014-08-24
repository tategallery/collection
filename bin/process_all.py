'''
	Go through all artwork jsons and produce an index for
	level0, level1, level2

	Does not preserve relationships between the levels
'''


import json
from os import walk

# use dict to elimiate duplicated entries as new entries
# are added as {'value of id': 'value of name'}
level0 = {}
level1 = {}
level2 = {}

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

		for child in subjects0:
			subjects1 = child['children']
			level0[child['id']] = child['name']

			for child in subjects1:
				subjects2 = child['children']
				level1[child['id']] = child['name']

				for child in subjects2:
					level2[child['id']] = child['name']

def write_files(dict, filename):
	jsondata = json.dumps(dict,sort_keys = True,separators = (',',':'))
	output = open('../processed/' + filename,'w')
	output.writelines(jsondata)
	output.close

open_files('../artworks')

write_files(level0,'level0.json')
write_files(level1,'level1.json')
write_files(level2,'level2.json')