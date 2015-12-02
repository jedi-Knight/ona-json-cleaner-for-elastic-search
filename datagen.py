#!/usr/bin/python3

import json
import re
from copy import deepcopy
import hashlib
import sys
import datetime
import random

itemArray = open(sys.argv[1], 'r')

gendatafile = open('data.gen.'+sys.argv[1], 'w')

start = 0
size = 1000

startdate = datetime.datetime.now()

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
	dataSet['_submission_time'] = (startdate+datetime.timedelta(seconds=14.4*c)).strftime('%Y-%m-%dT%H:%M:%S')
	dataSet['building_damage_assessment/hh_data/hh_address/hh_address_district/district'] = c%14
	dataSet['_geolocation'] = [random.uniform(84.4929481, 86.9713082), random.uniform(27.5705217, 28.6946975)]
	del dataSet['_uuid']
	#dataSet['_uuid'] = os.popen("md5sum <<'"+str(c)+"'").read().replace('\n', '')
	dataSet['_uuid'] = hashlib.md5(json.dumps(dataSet).encode('utf-8')).hexdigest()
	gendata.append(dataSet)

gendatafile.write(json.dumps(gendata))








