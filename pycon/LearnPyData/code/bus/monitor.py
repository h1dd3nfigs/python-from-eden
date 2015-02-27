# monitor.py
#
# Periodically monitor the bus system and see whether an identified
# bus returns to within a half-mile of Dave's office

import urllib
from xml.etree.ElementTree import parse
import time
import webbrowser

# Latitude of Dave's office.
office_lat = 41.980262

# Set of bus ids that you want to monitor.  Change to match
# the output of the find_north.py script

# the bus with id 4140 had a lat closest to the office_lat 
# at the time the rt22.xml feed was generated so 
# that bus is the best candidate for the one travis rode
# so let's just monitor the lat location of that bus in this script
busids = { '4140' }

def distance(lat1, lat2):
    'Return approx miles between lat1 and lat2'
    return 69 * abs(lat1 - lat2)

def check():
    # cta unofficial api
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in busids:
            lat = float(bus.findtext('lat'))
            lon = float(bus.findtext('lon'))
            dist = distance(lat, office_lat)
            direction = bus.findtext('d')
            print('%s %s %0.2f miles' % (busid, direction, dist))
            
            if dist < 0.5:
                # Launch a browser to see on a map
                chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
                webbrowser.get(chrome_path).open('http://maps.googleapis.com/maps/api/staticmap?size=500x500&sensor=false&markers=|%f,%f' % (lat, lon))
while True:
    check()
    # Suspend execution of the current thread for the given number of second
    # aka pause for 60 sec before calling the check() method again
    time.sleep(60)

