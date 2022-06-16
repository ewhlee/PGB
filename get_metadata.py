import json
import xml.etree.ElementTree as ET
from Bio import Entrez

INPUT_PATH = '' # input path
OUTPUT_PATH = '' # output path

Entrez.email = '' # email address to access Entrez api

max_len = 10000
for i in range(0, 100):
	print('working:', i)
	f_in = open(INPUT_PATH.format(i), 'r')

	json_dict = dict()
	id_lst = list()
	for line in f_in:
		json_line = json.loads(line.strip())
		json_dict[json_line['pmid']] = json_line
		id_lst.append(json_line['pmid'])
	f_in.close()

	
	for j in range(0, len(id_lst), max_len):
		handle = Entrez.efetch(db="pubmed", id=','.join(map(str, id_lst[j:j+max_len])), rettype="xml", retmode="text")
		records = Entrez.read(handle)

		for pubmed_article in records['PubmedArticle']:
			medline = pubmed_article['MedlineCitation']
			article = pubmed_article['MedlineCitation']['Article']
			pubmed_data = pubmed_article['PubmedData']

			pmid = str(pubmed_article['MedlineCitation']['PMID'])
			if pmid not in json_dict:
				print('{} does not exist'.foramt(pmid))

			json_dict[pmid]['publication_type'] = list()
			if 'PublicationTypeList' in article:
				for name in article['PublicationTypeList']:
					json_dict[pmid]['publication_type'].append(name)

			json_dict[pmid]['chemicals'] = list()
			if 'ChemicalList' in medline:
				for chem_dict in medline['ChemicalList']:
					name = chem_dict['NameOfSubstance']
					json_dict[pmid]['chemicals'].append(name)

			json_dict[pmid]['mesh'] = list()
			if 'MeshHeadingList' in medline:
				for mesh_dict in medline['MeshHeadingList']:
					name = mesh_dict['DescriptorName']
					temp_major = mesh_dict['DescriptorName'].attributes['MajorTopicYN']
					is_major = True
					if temp_major == 'N':
						is_major = False
					temp_dict = dict()
					temp_dict['term'] = name
					temp_dict['is_major'] = is_major
					json_dict[pmid]['mesh'].append(temp_dict)

	f_out = open(OUTPUT_PATH.format(i), 'w')
	for pmid in id_lst:
		if 'publication_type' not in json_dict[pmid]:
			json_dict[pmid]['publication_type'] = list()
		if 'chemicals' not in json_dict[pmid]:
			json_dict[pmid]['chemicals'] = list()
		if 'mesh' not in json_dict[pmid]:
			json_dict[pmid]['mesh'] = list()
		f_out.write('{}\n'.format(json.dumps(json_dict[pmid])))

	f_out.close()