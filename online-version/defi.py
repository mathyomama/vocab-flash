import parse
import urllib2
import error



class Definition(object):
	"""This class takes a word and uses urllib2 to grab a file which is then parsed using Parse from parser."""


	def __init__(self, word):
		try:
			self.data = urllib2.urlopen("http://en.wiktionary.org/w/index.php?action=raw&title=%s" % word)
			self.definition = parse.Parser(self.data)
		except urllib2.HTTPError:
			self.http_error_message()

	def check_word(self, data):
		pass

	def http_error_message(self):
		print error.http_error

	def print_entry(self):
		print self.definition.get_entry()
