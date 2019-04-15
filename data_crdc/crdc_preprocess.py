import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import csv
import sqlite3

database = "../all_data.db"

read_data = []


def create_connection(db_file):

	try:
		conn = sqlite3.connect(db_file)
		return conn
	except:
		print("no")
		# print(e)
 
	return None


def add_data(cur, arr):

	sql = """ INSERT INTO crdc(
				dist_state_abbrev,
				dist_id, 
				dist_name,
				school_id,
				school_name,
				dist_and_school_id,
				ov_enr_hisp_m,
				ov_enr_hisp_f,
				ov_enr_ai_an_m,
				ov_enr_ai_an_f,
				ov_enr_as_m,
				ov_enr_as_f,
				ov_enr_nh_m,
				ov_enr_nh_f,
				ov_enr_b_m,
				ov_enr_b_f,
				ov_enr_w_m,
				ov_enr_w_f,
				ov_enr_twomr_m,
				ov_enr_twomf)
			VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
	"""
	cur.execute(sql, arr)
	conn.commit()
	return cur.lastrowid

conn = create_connection(database)
cur = conn.cursor()

# df = pd.read_csv('/users/amypu/documents/Data_Files_and_Layouts/CRDC 2015-16 School Data.csv')
with open('/users/amypu/documents/Data_Files_and_Layouts/CRDC_2015-16_School_Data.csv') as data:
	read_data = csv.reader(data)

# print("Column headings:")
# print(df.head())

	processed_data = []

	for line in read_data:
		# print(line[5])

		# only add to processed data if line[18] == Yes and line[19] == Yes and line[20] == Yes and line[21] == Yes
		if (line[18] == "Yes") and (line[19] == "Yes") and (line[20] == "Yes") and (line[21] == "Yes"):
			# print(line[5])
			district_state_abbrev = line[0] #district state abbreviation
			district_id = line[2] #7 digit district id
			district_name = line[3] #district name
			school_id = line[4] #5 digit school id
			school_name = line[5] #school name
			district_and_school_id = line[6] #7 digit district and 5 digit school id

			overall_enr_hisp_m = line[55] #overall student enrollment: hispanic male
			overall_enr_hisp_f = line[56] #overall student enrollment: hispanic female
			overall_enr_ai_an_m = line[57] #overall student enrollment: american indian/alaska native male
			overall_enr_ai_an_f = line[58] #overall student enrollment: american indian/alaska native female
			overall_enr_as_m = line[59] #overall student enrollment: asian male
			overall_enr_as_f = line[60] #overall student enrollment: asian female
			overall_enr_nh_m = line[61] #overall student enrollment: native hawaiian/pacific islander male
			overall_enr_nh_f = line[62] #overall student enrollment: native hawaiian/pacific islander female
			overall_enr_b_m = line[63] #overall student enrollment: black male
			overall_enr_b_f = line[64] #overall student enrollment: black female
			overall_enr_w_m = line[65] #overall student enrollment: white male
			overall_enr_w_f = line[66] #overall student enrollment: white female
			overall_enr_twomr_m = line[67] #overall student enrollment: two or more races male
			overall_enr_twomr_f = line[68] #overall student enrollment: two or more races female
			overall_enr_m_tot = line[69] #overall student enrollment: calculated male total
			overall_enr_f_tot = line[70] #overall student enrollment: calculated female total

			g_and_t = line[147] #gifted and talented indicator

			num_adv_ma = line[387] #number of advanced mathematics classes

			ap_ind = line[491] #AP indicator: does this student have any students in AP programs?

			num_ap_c = line[492] #number of different AP courses offered

			tot_ap_pass_m = line[631] #number of students who passed some AP exams: male
			tot_ap_pass_f = line[632] #number of students who passed some AP exams: female

			id_ind = line[657] #IB program indicator

			har_bul_sex = line[1327] #allegations of harrassment or bullying on the basis of sex
			har_bul_race = line[1328] #allegations of harrassment or bullying on the basis of race, color, or national origin
			har_bul_dis = line[1329] #allegations of harrassment or bullying on the basis of disability
			har_bul_sex_o = line[1330] #allegations of harrassment or bullying on the basis of sexual orientation
			har_bul_rel = line[1331] #allegations of harrassment or bullying on the basis of religion

			row = []
			row.append(district_state_abbrev)
			row.append(district_id)
			row.append(district_name)
			row.append(school_id)
			row.append(school_name)
			row.append(district_and_school_id)
			row.append(overall_enr_hisp_m)
			row.append(overall_enr_hisp_f)
			row.append(overall_enr_ai_an_m)
			row.append(overall_enr_ai_an_f)
			row.append(overall_enr_as_m)
			row.append(overall_enr_as_f)
			row.append(overall_enr_nh_m)
			row.append(overall_enr_nh_f)
			row.append(overall_enr_b_m)
			row.append(overall_enr_b_f)
			row.append(overall_enr_w_m)
			row.append(overall_enr_w_f)
			row.append(overall_enr_twomr_m)
			row.append(overall_enr_twomr_f)
			# row.append(g_and_t)
			# row.append(num_adv_ma)
			# row.append(ap_ind)
			# row.append(num_ap_c)
			# row.append(tot_ap_pass_m)
			# row.append(tot_ap_pass_f)
			# row.append(id_ind)
			# row.append(har_bul_sex)
			# row.append(har_bul_race)
			# row.append(har_bul_dis)
			# row.append(har_bul_sex_o)
			# row.append(har_bul_rel)
			

			# print(len(row))
			processed_data.append(row)

			x = add_data(cur, row[:])

print(np.array(processed_data).shape)

# def create_table(conn, sql_text):
# 	try:
# 		c = conn.cursor()
# 		c.execute(create_table_sql)
# 		c.close()
# 	except:
# 		print("nooooo")

# create_table_sql = """ CREATE TABLE IF NOT EXISTS crdc (
# 					id integer PRIMARY KEY,
# 					dist_state_abbrev TEXT, 
# 					dist_id integer,
# 					dist_name TEXT, 
# 					school_id integer,
# 					school_name TEXT,
# 					dist_and_school_id integer,
# 					ov_enr_hisp_m integer,
# 					ov_enr_hisp_f integer,
# 					ov_enr_ai_an_m integer,
# 					ov_enr_ai_an_f integer,
# 					ov_enr_as_m integer,
# 					ov_enr_as_f integer,
# 					ov_enr_nh_m integer,
# 					ov_enr_nh_f integer,
# 					ov_enr_b_m integer,
# 					ov_enr_b_f integer,
# 					ov_enr_w_m integer,
# 					ov_enr_w_f integer,
# 					ov_enr_twomr_m integer,
# 					ov_enr_twomf integer
# 				); """

# if conn is not None:
# 	create_table(conn, create_table_sql)
# else:
# 	print("ugh")