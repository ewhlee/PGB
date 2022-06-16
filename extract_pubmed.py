import json

input_name = '' # s2orc dataset path
output_name = '' # PGB dataset path

for i in range(0, 100):
	print('working: {}'.format(i))
	f_in = open(input_name.format(i), 'r')
	f_out = open(output_name.format(i), 'w')

	for line in f_in:
		json_line = json.loads(line)
		json_line.pop('arxiv_id')
		json_line.pop('acl_id')
		json_line.pop('pmc_id')
		json_line.pop('doi')
		json_line.pop('mag_id')
		json_line.pop('mag_field_of_study')
		json_line.pop('has_pdf_parse')
		json_line.pop('s2_url')

		new_json = dict()
		new_json['s2id'] = json_line['paper_id']
		new_json['pmid'] = json_line['pubmed_id']
		new_json['pmcid'] = json_line['pmc_id']
		new_json['title'] = json_line['title']
		new_json['abstract'] = json_line['abstract']
		new_json['authors'] = json_line['authors']
		new_json['year'] = json_line['year']
		new_json['venue'] = json_line['venue']
		new_json['journal'] = json_line['journal']
		new_json['outbound_citations'] = json_line['outbound_citations']
		new_json['inbound_citations'] = json_line['inbound_citations']
		new_json['has_outbound_citations'] = json_line['has_outbound_citations']
		new_json['has_inbound_citations'] = json_line['has_inbound_citations']

		if (json_line['pubmed_id'] is not None):
			f_out.write('{}\n'.format(json.dumps(new_json)))

	f_in.close()
	f_out.close()