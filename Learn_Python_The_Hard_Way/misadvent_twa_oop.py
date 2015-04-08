# python 2.7
# OOP approach to Misadventures of a Confused TWA
from random import shuffle

import misadvent_game_txt as txt 

scenes = []

# list of tuples describing each scene 
# (scene_name, keyword_to_be_guessed, intro_message)
scene_desc = [
			('big_chop', 'afro' , txt.big_chop_intro ),
			('braid_salon', 'edges', txt.braid_salon_intro),
			('blowout_salon', 'protectant', txt.blowout_salon_intro),
			('wig_store', 'elastic', txt.wig_store_intro),
			('home_hair_closet', 'kanekalon', txt.home_hair_closet_intro),
			('date', 'transitioning', txt.date_intro),
			('death', 'death' , 'intro to death'),
			
			]

class Scene(object):

	def __init__(self, name, keyword, intro):
		self.name = name
		self.keyword = keyword
		self.intro = intro

	# player confronts the villain and must guess the magic keyword
	# within the total number of tries or die 
	def confront(self, keyword):
		self.keyword = keyword
		riddle = self.scramble(self.keyword)

		total_tries = len(riddle) // 2
		attempt = 0
		prompt = "Defeat the villain by decoding the scrambled word: %s\v" % riddle 
		guess = raw_input(prompt)

		while guess != self.keyword and attempt < total_tries:
			attempt += 1
			print "Try again" 
			guess = raw_input(prompt)
		
		if guess == self.keyword:
			return "success"	
		else:
			return "failure"	

	# scramble the letters of the magic keyword and return the result
	def scramble(self, keyword):
		self.keyword = keyword
		keyword_list = list(self.keyword)
		shuffle(keyword_list)
		riddle = ''.join(keyword_list).upper()
		return riddle

class Game(object):
	
	def __init__(self, scenes):
		self.scenes = scenes
	
	def start(self):
		level = 0
		outcome = "success"
		print scenes[level].intro
		outcome = scenes[level].confront(scenes[level].keyword)
		while outcome == 'success' and level < len(scenes)-2:
			level += 1
			print scenes[level].intro
			outcome = scenes[level].confront(scenes[level].keyword)
		
		if outcome == "success":
			print txt.game_win_msg
		else:
			print scenes[-1].name


for i in range(len(scene_desc)):
	name , keyword, intro = scene_desc[i]
	new_scene = Scene(name, keyword, intro)
#	print "Adding scene %s to position %d of scenes" % (new_scene.name, i)
	scenes.append(new_scene)

# Main
if __name__ == '__main__':
	a_game = Game(scenes)
	a_game.start()