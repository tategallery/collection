'''
	For AR experiment
	Using the level2list.json as index and the artworks jsons as content
	associate AR artworks with index

	outputs json of acno for each object in level2list
	only if that index contains the artwork
'''

import json
from os import walk

level2list = json.loads(open('../processed/level2list.json').read().decode('utf-8'))
level2listfinal = []

# make space for the artwork no.
# each row has one artlist associated
def init():
	for row in level2list:
		row['artlist'] = []

def open_art_files(targetpath):
	for dirname, dirnames, filenames in walk(targetpath):

		for filename in filenames:

			filepath = '/'.join([dirname,filename])
			fileopen = open(filepath).read().decode('utf-8')
			jsonopen = json.loads(fileopen)

			acno = jsonopen['acno']
			title = jsonopen['title']
			thumbnail =jsonopen['thumbnailUrl']
			url = jsonopen['url']

			contributorCount = jsonopen['contributorCount']

			if contributorCount is 1:
				artist = jsonopen['contributors'][0]['fc']
			else:
				artistlist = []
				for c in jsonopen['contributors']:
					contrib.append(c['fc'])
				artist = ' ,'.join(artistlist)

			subjectCount = jsonopen['subjectCount']

			if subjectCount is not 0 and thumbnail is not None:
				subjects0 = jsonopen['subjects']['children']

				for child0 in subjects0:
					subjects1 = child0['children']

				for child1 in subjects1:
					subjects2 = child1['children']

				for child2 in subjects2:
					item = {}
					item['id'] = acno
					item['title'] = title
					item['artist'] = artist
					item['url'] = url
					# open txt files with base64 encode for a 40x40 thumbnail
					item['thumb'] = open_matching_base64_file(acno)
					matchdict = next((item for item in level2list if item['id'] == child2['id']), None)
					# add the acno to the corresponding jsonopen
					matchdict['artlist'].append(item)

def open_matching_base64_file(matchingid):
	try:
		txtopen = open('./images0/ar40/' + matchingid + '.tile.txt','rb')
		txtcontent = txtopen.read()
		return txtcontent
	except:
		return 'none'

def finish():
	for row in level2list:
		if len(row['artlist']):
			level2listfinal.append(row)

def write_file(data, filename):
	jsondata = json.dumps(data,sort_keys = True,separators = (',',':'))
	output = open('../processed/' + filename,'w')
	output.writelines(jsondata)
	output.close

init()
open_art_files('../artworks/ar')
finish()
write_file(level2listfinal,'level2list_ar.json')
