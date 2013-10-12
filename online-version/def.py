import parser
import urllib2



class definition(object):
	"""This class takes a word and uses urllib2 to grab a file which is then parsed using Parse from parser."""


	def __init__(self, word):
		self.data = urllib2.urlopen("http://en.wiktionary.org/w/index.php?action=raw&title=%s" % word)
	

	def check_word(self, word):
		pass
