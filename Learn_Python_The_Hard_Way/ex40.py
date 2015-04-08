class Song(object):
	def __init__(self, lyrics, filler):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print filler, line

filler = "cha cha cha/n"

bday_lyrics = ["Happy birthday to you", 
					"I don't want to get sued",
					"So I'll stop right there",
					]
happy_bday = Song(bday_lyrics, filler)

bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells",
						], filler)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()