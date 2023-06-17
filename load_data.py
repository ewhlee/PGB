import json

FILENAME = ''

data = list()
with open(FILENAME, 'r') as f:
	for line in f:
		data.append(json.loads(line.strip()))