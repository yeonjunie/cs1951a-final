read_data = []
with open('/users/amypu/documents/Data_Files_and_Layouts/CRDC 2015-16 School Data.csv', 'r') as datafile:
	for line in datafile:
		read_data.append(line)

processed_data = []


for line in read_data:

	# only add to processed data if line[18] == Yes and line[19] == Yes and line[20] == Yes and line[21] == Yes
	if (line[18] == "Yes") and (line[19] == "Yes") and (line[20] == "Yes") and (line[21] == "Yes"):
		processed_data.append(line)