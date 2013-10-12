import parser
import StringIO
import re



class Section(object):
	"""This is the parent class for all the sections parsed out of Parse"""

	def __init__(self, heading, information):
		self.heading = heading
		self.information = information
		super(Heading, self).__init__(**kwargs)
	
	def get_heading(self):
		return self.heading

	def get_information(self):
		return self.information

	def get_formatted_information(self):
		pass


class Language(Section):
	"""This will dissect headings of languages like English"""

	def __init__(self, heading, information):
		super(Language, self).__init__(heading, information)


class Pronunciation(Section):
	"""This subclass handles the sections labeled pronunciation"""

	pass


class Etymology(Section):
	"""This subclass handles the etymology sections"""

	pass


class PartOfSpeech(Section):
	"""This is the subclass which handles all the parts of speech"""

	def __init__(self, heading, information):
		super(PartOfSpeech, self).__init__(heading, information)
	
	def get_formatted_information(self):
		pass


class Noun(PartOfSpeech):
	"""A class for the section labeled 'Noun'"""

	def __init__(self, heading, information):
		super(Noun, self).__init__(heading, information)


class Verb(PartOfSpeech):
	"""A class for the section labeled 'Verb'"""

	def __init__(self, heading, information):
		super(Verb, self).__init__(heading, information)


class Adjective(PartOfSpeech):
	"""A class for the section labeled 'Adjective'"""

	def __init__(self, heading, information):
		super(Adjective, self).__init__(heading, information)


class Adverb(PartOfSpeech):
	"""A class for the section labeled 'Adverb'"""

	def __init__(self, heading, information):
		super(Adverb, self).__init__(heading, information)


class Pronoun(PartOfSpeech):
	"""A class for the section labeled 'Pronoun'"""

	def __init__(self, heading, information):
		super(Pronoun, self).__init__(heading, information)


class Preposition(PartOfSpeech):
	"""A class for the section labeled 'Preposition'"""

	def __init__(self, heading, information):
		super(Prepostion, self).__init__(heading, information)


class Conjunction(PartOfSpeech):
	"""A class for the section labeled 'Conjunction'"""

	def __init__(self, heading, information):
		super(Conjunction, self).__init__(heading, information)


class Interjection(PartOfSpeech):
	"""A class for the section labeled 'Interjection'"""

	def __init__(self, heading, information):
		super(Interjection, self).__init__(heading, information)


class Synonyms(Section):
	"""Handles synonyms"""

	pass
