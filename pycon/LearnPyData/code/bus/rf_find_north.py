# find_north.py
#
# Parse the 'rt22.xml' file and identify all buses traveling
# northbound of Dave's office

office_lat = 41.980262 # latitute is N to S, so North > 41
office_lon = -87.668452 # longitude is East to West

# Import the xml element tree module so I can parse the transit
# xml file into usable objects
from xml.etree.ElementTree import parse

# since I imported parse above, no need to call it in the long format
# xml.etree.ElementTree.parse()
# line below parses the rt22.xml file into an element tree. 
# then we assign this tree to the variable doc
doc = parse('rt22.xml')
# look at the doc element tree and findall() finds every element
# with the tag 'bus' and assign it to the loop variable also called bus
for bus in doc.findall('bus'):
	#look at the lat value for each bus element
	# findtext() finds text for the first subelement matching the argument, 'lat'
	# in other words for subelement of bus, look for element named lat 
	# and assign it's value to a variable named lat
	lat = float(bus.findtext('lat'))
	# if the latitude value of a bus is greater than or north of the office,
	if lat > office_lat:
		busid = bus.findtext('id')
		direction = bus.findtext('d')
		if direction.startswith('North'):
		# output every element with the tag 'bus' and the lat subelemeent's value
			print lat, busid, direction


# The output above is which bus Travis was likely on
# Now I need to real-time track where that bus would 
# now to hopefully meet up with him
# step 1: Figure out which bus he was on

# step 2: Tell us when that bus (bus id printed above)
# willbe a  distance that is 0.5 mi from here (office_lat)

# 1- create a program that periodically visits bustracker site (10min)
# 2- run urllib.open('cta bus tracker url') to exact bus locations 
# for each moment
# 3- parse and find lat for bus id specificed in step 1 way above
# 4- calculate which lat position = 0.5 mi north of office
# 5- if lat position <= 0.5mi at time of parse & bus direction is south
# then open browser to next bus stop location on google maps



    
