read_data = []
with open('FRSS108PUF.dat', 'r') as datafile:
    for line in datafile:
        read_data.append(line)

# each line has 1442 chars, 1527 lines total

# weird lines: 140, 330, 364, 370, 383, ... just a lot of 1.12

processed_data = []

for line in read_data:
    idn = line[0:6]
    dist_size = line[6]
    urb = line[7]
    reg = line[8]



# print(len(read_data))

# todo -- create some sort of a data object?