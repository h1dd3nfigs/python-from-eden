import textwrap
import misadvent_game_txt as txt 



class Room:
  
	def __init__(self, name, intro, prompt, exit, optional_arg=None):
		self.name = name
		self.intro = intro
		self.prompt = prompt
		self.exit = exit
		if optional_arg is None:
			optional_arg = ['default',]
		self.optional_arg = optional_arg

ROOMSLIST = [Room('AF Salon', 
	          txt.af_salon_intro, 
	          txt.af_salon_prompt, 
	          txt.af_salon_exit),

         Room('Dom Salon',
	          txt.dom_salon_intro, 
	          txt.dom_salon_prompt, 
	          txt.dom_salon_exit),

        Room('Home Wig',
        	 txt.home_wig_intro, 
	         txt.home_wig_prompt, 
	         txt.home_wig_exit),

        Room('Home Crochet',
        	txt.home_crochet_intro, 
            txt.home_crochet_prompt, 
            txt.home_crochet_exit),
]

ROOMSDICT = {room.name: room for room in ROOMSLIST}


def start():     
	print "\n\tMisadventures of a Confused TWA Natural\n"
	
	wrapper = textwrap.TextWrapper(initial_indent='\t', subsequent_indent='\t')

	print wrapper.fill(txt.start_txt)

	invite = raw_input("\t")

	if "accept" in invite or "yes" in invite:		
		pick_stylist()
	
	elif "decline" in invite or "no" in invite:
		dead('\tPanic and never say anything to him ever again.') 
			
	else :
		dead('\tNot sure how you\'re responding to his invite')

def pick_stylist():
	budget = int(raw_input("\tWhat's your budget for looking good?  $"))
	time = int(raw_input("\tHow many hours are you willing to invest in stying your hair?  "))
		
	if budget >= 50 and time >= 4:
		african_salon()
	elif budget >= 50 and time < 4:
		dominican_salon()
	elif budget < 50 and time >= 4:
		home_crochet()
	else:
		home_wig()	

def african_salon():

	wrapper = textwrap.TextWrapper(initial_indent='\t', subsequent_indent='\t')
	
	print "\n\n",wrapper.fill(ROOMSDICT['AF Salon'].intro)

	total_braids = 3	

	for x in range(total_braids):
		invite = raw_input(txt.af_salon_prompt)

		if "accept" in invite:		
			dead(txt.af_salon_exit)	

		elif "refuse" in invite:
			print "You run out of the salon. Do you wanna try another salon or just DIY at home?" 
			decide = raw_input("\t")
			if "salon" in decide:
				dominican_salon()
				break
			else:
				home_wig()
				break
		else : # you reason with her so repeat this loop
			print 'another braid down ', total_braids -1 , 'to go'
			total_braids -= 1
	else:
		dead(txt.af_salon_exit)	


def dominican_salon():

	wrapper = textwrap.TextWrapper(initial_indent='\t', subsequent_indent='\t')
	
	print "\n\n",wrapper.fill(txt.dom_salon_intro)

	num_iron_pass = 3

	for x in range(num_iron_pass):
		invite = raw_input(txt.dom_salon_prompt)
	
		if "yes" in invite:
			print "She spritzes some heat protectant spray and smoothes on an alcohol-rich, edge control. Then she runs the sections of your leave-out between the hot plates. Still not straight enough to match."

		else:
			dead(txt.dom_salon_exit)
	else:
		print "You're crispy hair broke off from heat damage."
		dead(txt.dom_salon_exit)

def home_wig():
	wrapper = textwrap.TextWrapper(initial_indent='\t', subsequent_indent='\t')
	
	print "\n\n",wrapper.fill(txt.home_wig_intro)

	invite = raw_input(txt.home_wig_prompt)

	if "tease" in invite:		
		dead(txt.home_wig_exit)	
	else : 
		dead(txt.home_wig_exit)	
	 

def home_crochet():
	wrapper = textwrap.TextWrapper(initial_indent='\t', subsequent_indent='\t')
	
	print "\n\n",wrapper.fill(txt.home_crochet_intro)

	num_sections = 3

	for x in range(num_sections):
		invite = raw_input(txt.home_crochet_prompt)
	
		if "yes" in invite:
			print "Power through the pain to braid & crochet another section."

		else:
			dead(txt.home_crochet_exit)
	else:
		dead(txt.home_crochet_exit)

def dead(why):
	print why
	exit(0)

start()






