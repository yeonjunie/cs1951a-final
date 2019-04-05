import numpy as np

read_data = []
with open('/users/amypu/documents/Data_Files_and_Layouts/CRDC 2015-16 School Data.csv', 'r') as datafile:
	for line in datafile:
		read_data.append(line)

processed_data = []

for line in read_data:

	# only add to processed data if line[18] == Yes and line[19] == Yes and line[20] == Yes and line[21] == Yes
	if (line[18] == "Yes") and (line[19] == "Yes") and (line[20] == "Yes") and (line[21] == "Yes"):
		# 7 digit district id
		district_id = line[2]
		# 5 digit school id
		school_id = line[4]
		# gifted and talented indicator
		g_and_t = line[147]

		processed_line = line[2] + line[4] + line[147:]
		processed_data.append(processed_line)

print(np.array(processed_data).shape)
