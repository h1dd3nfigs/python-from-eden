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
pothole_lookup_table = list(csv.DictReader(pothole_file))