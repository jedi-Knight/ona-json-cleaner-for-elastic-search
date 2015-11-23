#!/usr/bin/python3

import json
import re

itemArray = open('hda.json', 'r')

keyshorteneddatadumpFile = open('hda.keyshortenened.json','w')
keymappingFile = open('hda.keydef.json', 'w')

itemArray = itemArray.read()

itemArray = json.loads(itemArray)

keyDictionary = {}

keyShortenedDatadump = []

clashAvoidedCount = 0

for index, item in enumerate(itemArray):
	tempKeyDictionary = {}
	itemHolder = {}
	for k,v in item.items():
		subK = re.sub(r'^_', r'', k)
		subK = re.sub(r'(^.).*(.)/(\w+$)', r'\1_\2_\3', subK)
		if subK not in tempKeyDictionary:
			tempKeyDictionary[subK] = k
			itemHolder[subK] = v
		else:
			clashAvoidedCount += 1
			tempKeyDictionary[subK+str(clashAvoidedCount)] = k
			itemHolder[subK+str(clashAvoidedCount)] = v
	keyDictionary.update(tempKeyDictionary)
	keyShortenedDatadump.append(itemHolder)	

keymappingFile.write(json.dumps(keyDictionary))

keyshorteneddatadumpFile.write(json.dumps(keyShortenedDatadump))

print(clashAvoidedCount)







