import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from sqlite3 import Error


read_data = []
with open('frss92.dat', 'r') as datafile:
    for line in datafile:
        read_data.append(line)

# each line has 1442 chars, 1527 lines total
# quality measures? sum of 10-77
# barrier measures? 80-93 (providing), 96-111 (student participation)
# resource limitations for adding + phasing out? 118-123 (adding), 138-143 (removing)
# all of the above aren't zero-indexed (based on key provided w dataset)

processed_data = []


def get_score(subarr):
    score = 0
    for elt in subarr:
        if (elt not in [" ", "-", "8"]):
            score += int(elt)
    return score

for line in read_data:

    idn = int(line[1:5])

    if(line[6] == "2"):

        # joinable attributes
        dist_size = line[7] # 1 = less than 2500k, 2 = 2500k < 9999k, 3 = 10000k+
        urb = line[8] # 1 = city, 2 = suburban, 3 = town, 4 = rural
        region = line[9] # 1 = northeast, 2 = southeast, 3 = central, 4 = west

        # response vars
        totalComputers = get_score(line[16-19])
        computersForInstruction = get_score(line[24-27])
        integration = get_score(line[135]) # on a range of 1-4 if district staff help technology integration
        training = get_score(line[154])

        # add to processed_data
        dist_data = [idn, dist_size, urb, region, totalComputers, computersForInstruction, integration, training]
        processed_data.append(dist_data)


# no nulls in data

print(len(processed_data)) # = 916
print(len(processed_data[0])) # = 8

database = "all_data.db"

columns = ('idn', 'dist_size', 'urb', 'region', 'totalComputers', 'computersForInstruction', 'integration', 'training')

def create_connection(db_file):
    try :
        # connection = sqlite3.connect("edTech.db")
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    # finally:
    #     connection.close()
    return connection

def create_table(conn, sql_text):
    try:
        c = conn.cursor()
        c.execute(districtTable)
        c.close()
    except Error as e:
        print(e)

districtTable  = """ CREATE TABLE IF NOT EXISTS edtech(
    dist_size integer,
    urb integer,
    region integer,
    totalComputers integer NOT NULL ,
    computersForInstruction integer ,
    integration integer,
    training integer,
    idn integer PRIMARY KEY
);"""

connection = create_connection("database.db")

if connection is not None:
    create_table(connection, "database.db")
else:
    print("Not connecting")

