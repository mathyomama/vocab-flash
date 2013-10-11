import parser
import StringIO


class Heading(object):
	"""This is the parent class for all the sections parsed out of Parse"""

	def __init__(self, heading, information):
		self.heading = heading
		self.information = information
		super(Heading, self).__init__(**kwargs)
	
	def get_heading(self):
		return self.heading

	def get_information(self):
		return self.information


class Language(Heading):
	"""This will dissect headings of languages like English"""

	def __init__(self, heading, information):
		super(Language, self).__init__(heading, information)


class PartOfSpeech(Heading):
	"""This is the subclass which handles all the parts of speech"""

	def __init__(self, heading, information):
		super(PartOfSpeech, self).__init__(heading, information)
	
	def get_definitions(self):
		buff = StringIO.StringIO(self.information)

