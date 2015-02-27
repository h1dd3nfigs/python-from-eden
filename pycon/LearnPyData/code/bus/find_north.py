# find_north.py
#
# Parse the 'rt22.xml' file and identify all buses traveling
# northbound of Dave's office

office_lat = 41.980262 # North to South, so North > 41
office_longitude = -87.668452 # East to West

from xml.etree.ElementTree import parse

doc = parse('rt22.xml')
for bus in doc.findall('bus'):
    lat = float(bus.findtext('lat'))
    if lat >= office_lat:
        busid = bus.findtext('id')
        direction = bus.findtext('d')
        if direction.startswith('North'):
            print(busid, direction, lat)

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

    
