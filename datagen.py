#!/usr/bin/python3

import json
import re
from copy import deepcopy
import hashlib
import sys

itemArray = open(sys.argv[1], 'r')

gendatafile = open('data.gen.'+sys.argv[1], 'w')

start = 0
size = 1000

try:
	start = int(sys.argv[2])
	size = start+1000
except:
	print('ok')

try:
	size = int(sys.argv[3])
except:
	print('ok again')

itemArray = itemArray.read()

itemArray = json.loads(itemArray)

gendata = []

defSet = {}

for index, item in enumerate(itemArray):	
	for k,v in item.items():
		defSet[k] = v

for c in range(start, start+size):
	dataSet = deepcopy(defSet)
	dataSet['_id'] = c
	del dataSet['_uuid']
	#dataSet['_uuid'] = os.popen("md5sum <<'"+str(c)+"'").read().replace('\n', '')
	dataSet['_uuid'] = hashlib.md5(json.dumps(dataSet).encode('utf-8')).hexdigest()
	gendata.append(dataSet)

gendatafile.write(json.dumps(gendata))








