name = 'Zed A. Shaw .'
age = 35 # not a lie
height = 74 # inches
in_to_cm_conversion = 2.54
metric_height = height * in_to_cm_conversion # cm

weight = 180 # lbs
lb_to_kg_conversion = 0.54
metric_weight = weight * lb_to_kg_conversion # kg

eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall OR %f cm tall. " % (height, metric_height)
print "He's %d pounds heavy OR %f kg strong :-) " % (weight, metric_weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair. " % (eyes, hair)
print "His teeth are usually %s depending on the coffee. " %teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d. " % (age, height, weight, age + height + weight)