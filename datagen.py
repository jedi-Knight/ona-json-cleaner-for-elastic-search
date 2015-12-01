#!/usr/bin/python3

import json
import re
from copy import deepcopy
import os

itemArray = open('hda.json', 'r')

gendatafile = open('data.json','w')

itemArray = itemArray.read()

itemArray = json.loads(itemArray)

gendata = []

defSet = {}

for index, item in enumerate(itemArray):	
	for k,v in item.items():
		defSet[k] = v

for c in range(0,100):
	defSet['_id'] = c
	del defSet['_uuid']
	gendata.append(defSet)
	defSet['_uuid'] = os.popen("md5sum <<'"+json.dumps(defSet)+"'").read().replace('\n', '')

gendatafile.write(json.dumps(gendata))








