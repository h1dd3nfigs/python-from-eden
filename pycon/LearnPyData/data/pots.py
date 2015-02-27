# Task 2: Find the five most post-apocalyptic 
# pothole-filled 10-block sections of road in Chicago
# using the city's open data

# I imagine accomplishing this by 
# 1) import the csv containing all 140k rows of data
# 2) create a lookup table so I can ID the number of holes potholes filled 
# based on the street address or zipcode I lookup
# 3) perhaps first narrow down which zipcode has the most
# by sorting my lookup table by zipcode and tabulating potholes for each zip
# 4) then within that zipcode, narrow down to the street address
# to get broader street address rename the number in street address from 328 to 3XX 
# then tabulate potholes for each hundreds street address in this zip 
# 5) insert error handling or exception handling for missing data??



# read the data and perform a calculation
import csv

pothole_file = open('potholes.csv','r')
# Create a Dictionary out of the csv read into the variable pothole_file
pothole_dict = list(csv.DictReader(pothole_file))

# create empty dict where key will be zip and value will be number of potholes
num_potholes_by_zip = {}

#create a for loop that adds up the number of potholes for each zip
for row in pothole_dict:
 	zipcode = row['ZIP']
 	status = row['STATUS']
 	# Check whether a zipcode key is already in our dict before starting a new key for it
	if status == 'Open':
		if zipcode in num_potholes_by_zip:
			num_potholes_by_zip[zipcode] += 1
		else:
			num_potholes_by_zip[zipcode] = 1
			

# Now to print a table with the number of potholes per zipcode
print 'Number of potholes by zipcode: '
#iterate over each key, aka zipcode, of a dict sorted by value
# I could either run the 2 lines directly below or use lines 50-52
#for x in sorted(num_potholes_by_zip, key=num_potholes_by_zip.get):
#	print x, num_potholes_by_zip[x]

# Since python can't sort a dictionary, I can turn my dictionary into a list of tuples
# and then sort this list of tuples
# start by creating an empty list
rows = []
for key in num_potholes_by_zip.keys():
	rows.append((num_potholes_by_zip[key], key))

# sorted() method then sorts the list of tuples by the first element
# which in this case is num_potholes
print sorted(rows)

#grab the zipcode with the most potholes
baddest_zip = max(num_potholes_by_zip, key=num_potholes_by_zip.get)

# I manually added these zipcodes with the most potholes and should
# iterate over each zip down below when performing potholes by address counting
# but I got too lazy and ended up just using 60619, specified above as the 
# baddest_zip becaues it has the most potholes
bad_zips = ['60617','60620','60639', '60628','60619']

#filter the original pothole dict to only contain addresses with the baddest zip
bad_zip_dict = [s for s in pothole_dict
					if s['ZIP']==str(baddest_zip)]

# create empty dict where key will be hundreds street address and value will be number of potholes
num_potholes_by_street_address = {}

# perhaps ignore street numbers altogether and just go by street names for now 
for row in bad_zip_dict:
	# assign the csv's street address to variable named street_address
	street_address = row['STREET ADDRESS']
	# split the street_address string wherever there are spaces 
	address_parts = street_address.split(' ')
	# the first element in the list resulting from that string split is the address number
	# strip the last two chars in the address num and replace them with XX
	# so 355 becomes 3XX
	address_parts[0] = address_parts[0][:-3] + 'XXX'
	#rejoin the new XX address number with the rest of the address by calling
	#sep.join(parts) where my sep will be a space or ' '
#	hundreds_address = ' '.join(address_parts)
	thousands_address = ' '.join(address_parts)
	
	status = row['STATUS']
	if status == 'Open':
		if thousands_address in num_potholes_by_street_address:
			num_potholes_by_street_address[thousands_address] += 1
		else:
			num_potholes_by_street_address[thousands_address] = 1

# print a table with the number of potholes by hundreds address, sorted by # of potholes
print 'Number of potholes by hundreds_address'
for x in sorted(num_potholes_by_street_address, key=num_potholes_by_street_address.get):
	print x, num_potholes_by_street_address[x]