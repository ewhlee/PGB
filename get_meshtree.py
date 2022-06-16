import json

mtree_file = "mtrees2022.bin" # mesh tree file
input_file = "" # input json path
output_file = "" # output json path

mtree_dict = dict()
with open(mtree_file, 'r') as f:
	for line in f:
		row = line.strip().split(";")
		mtree_dict[row[0]] = row[1]

for i in range(0, 100):
	print(f"working: {i}")

	f_in = open(input_file.format(i), 'r')
	f_out = open(output_file.format(i), 'w')

	for line in f_in:
		json_line = json.loads(line)

		json_line['has_outbound_citations'] = False
		if len(json_line['outbound_citations']) > 0:
			json_line['has_outbound_citations'] = True

		json_line['has_inbound_citations'] = False
		if len(json_line['inbound_citations']) > 0:
			json_line['has_inbound_citations'] = True

		for mesh in json_line['mesh']:
			mesh['tree_num'] = ""
			if mesh['term'] in mtree_dict:
				mesh['tree_num'] = mtree_dict[mesh['term']]

		f_out.write(f"{json.dumps(json_line)}\n")

f_in.close()
f_out.close()