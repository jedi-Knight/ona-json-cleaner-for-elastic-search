#!/usr/bin/python3

import json
import re

itemArray = open('hda.json', 'r')

itemArray = itemArray.read()

itemArray = json.loads(itemArray)

keyDictionary = {}

clashAvoidedCount = 0

for index, item in enumerate(itemArray):
	tempKeyDictionary = {}
	for k,v in item.items():
		subK = re.sub(r'^_', r'', k)
		subK = re.sub(r'(^.).*(.)/(\w+$)', r'\1_\2_\3', subK)
		if subK not in tempKeyDictionary:
			tempKeyDictionary[subK] = k
		else:
			clashAvoidedCount += 1
			tempKeyDictionary[subK+str(clashAvoidedCount)] = k
	keyDictionary.update(tempKeyDictionary)
print(keyDictionary)












