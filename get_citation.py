import json

INPUT_PATH = '' # input path
ID_PATH = '' # semantic_scholar_id to pmid mapping
OUTPUT_PATH = '' # output path

pubmed_dict = dict()
f = open(ID_PATH, 'r')
print('reading ids')
for line in f:
	row = line.strip().split()
	pubmed_dict[row[0]] = row[1]
f.close()



for i in range(0, 100):
	print('writing:', i)
	f_in = open(INPUT_PATH.format(i), 'r')
	f_out = open(OUTPUT_PATH.format(i), 'w')
	for line in f_in:
		json_line = json.loads(line)
		
		new_json = dict()
		new_json['pmid'] = json_line['pmid']
		new_json['pmcid'] = json_line['pmcid']
		new_json['title'] = json_line['title']
		new_json['abstract'] = json_line['abstract']
		new_json['authors'] = json_line['authors']
		new_json['year'] = json_line['year']
		new_json['venue'] = json_line['venue']
		new_json['journal'] = json_line['journal']
		new_json['has_outbound_citations'] = json_line['has_outbound_citations']
		new_json['has_inbound_citations'] = json_line['has_inbound_citations']
		new_json['outbound_citations'] = list()
		new_json['inbound_citations'] = list()

		if len(json_line['outbound_citations']) > 0:
			for s2id in json_line['outbound_citations']:
				if s2id in pubmed_dict:
					new_json['outbound_citations'].append(pubmed_dict[s2id])
			
		if len(json_line['inbound_citations']) > 0:
			for s2id in json_line['inbound_citations']:
				if s2id in pubmed_dict:
					new_json['inbound_citations'].append(pubmed_dict[s2id])
		
		f_out.write('{}\n'.format(json.dumps(new_json)))

	f_in.close()
	f_out.close()
