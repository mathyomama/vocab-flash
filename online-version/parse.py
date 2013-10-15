import re
import urllib2
import section



class Parser(object):
	"""This is giant class which will handle the giant string, called source, generated by the urllib read function."""


	#A dictionary for the headings as read from the wiktionary file and the classes in String form
	useful_headings = [
			#languages
			"English",
			#PartOfSpeech
			"Noun",
			"Verb",
			"Adjective",
			"Adverb",
			"Pronoun",
			"Preposition",
			"Conjunction",
			"Interjection",
			"Pronunciation",
			#Etymology
			"Etymology",
			#Synonyms
			"Synonyms",
			]


	def __init__(self, data):
		self.data = data
		self.sections = self.split(self.data)
		self.list_of_section_objects = self.classify(self.sections)
		self.entry = self.make_entry(self.list_of_section_objects)

	def split(self, data):
		"""This takes the file-like object and splits the data into a dictionary with the headings as keys and information as values."""
		sections = list()
		equal = re.compile(r"^=+.*=+$")
		heading = ""
		information = ""
		for line in data:
			if re.match(r"^----$", line) != None:
				break
			result = equal.match(line)
			if result == None:
				information += line
				continue
			else:
				sections.append((heading, information))
				heading = result.group().strip('=')
				information = ""
		return sections
	
	def classify(self, sections):
		"""This method translates the list created by split and creates Section objects such as Noun or Pronunciation (or 'classifies' them)."""
		list_of_section_objects = []
		for section in sections:
			#Each element of section is a tuple with heading and unformatted information as the pair
			stripped_heading = section[0].rstrip(' 0123456789')
			if stripped_heading in self.useful_headings:
				list_of_section_objects.append(eval("%s(section[0], section[1])" % stripped_heading))
		return list_of_section_objects

	def make_entry(self, list_of_section_objects):
		entry = ''
		for sect in list_of_section_objects:
			entry += sect.get_section()
		return entry

	def get_entry(self):
		return self.entry
	
	def get_data(self):
		return self.data
	
	def get_sections(self):
		return self.sections

	def get_headings(self):
		return [section[0] for section in self.sections]


class Section(object):
	"""This is the parent class for all the sections parsed out of Parse"""

	def __init__(self, heading, information):
		self.heading = heading
		self.information = information
	
	def get_heading(self):
		return self.heading

	def get_information(self):
		return self.information

	def format_information(self, information):

		#A function for the substitution function...Naaaawwwwwt. Don't need it. I thought I was going to be cool by putting a function in a function
		string = information
		formatted_string = ""
		lines = string.split("\n")
		link = re.compile(r"\[\[(?P<word>\w.*?)\]\]")
		for line in lines:
			formatted_line = link.sub("\g<word>", line)
			formatted_string = str().join((formatted_string, formatted_line, '\n'))
		return formatted_string
			
	
	def get_formatted_information(self):
		return self.format_information(self.information)

	def get_section(self):
		return self.get_heading() + "\n" + self.get_formatted_information()


class Language(Section):
	"""This will dissect headings of languages like English"""

	def __init__(self, heading, information):
		super(Language, self).__init__(heading, information)


class English(Language):
	"""This is a subclass for Language, pretty much every word will use the English form"""

	def __init__(self, heading, information):
		super(English, self).__init__(heading, information)


class Pronunciation(Section):
	"""This subclass handles the sections labeled pronunciation"""

	def __init__(self, heading, information):
		super(Pronunciation, self).__init__(heading, information)


class Etymology(Section):
	"""This subclass handles the etymology sections"""

	def __init__(self, heading, information):
		super(Etymology, self).__init__(heading, information)


class PartOfSpeech(Section):
	"""This is the subclass which handles all the parts of speech"""

	def __init__(self, heading, information):
		super(PartOfSpeech, self).__init__(heading, information)
	
	def format_information(self, information):
		"""This method removes the curly braces which look like {context|<word>|lang=<lang.>}"""

		#A function for replacing context braces...Not, realized it wasn't necessary with capturing groups
		string = information
		#Using the parent method to remove the links from the string
		string = super(PartOfSpeech, self).format_information(string)
		formatted_string = ''
		lines = string.split("\n")
		legit_definition = re.compile(r"^# ")
		#not_definition = re.compile(r"^#[*:]")
		context = re.compile(r"{{(context|cx)\|(?P<con>.*?)\|lang=\w*?}}")
		definition_count = 0
		for line in lines:
			formatted_line = ''
			if legit_definition.match(line) != None:
				formatted_line = context.sub("(\g<con>)", line.lstrip("#"))
				definition_count += 1
			else:
				continue
			formatted_string = str().join((formatted_string, "%d" % definition_count, formatted_line, '\n'))
		formatted_string += "\n\n"
		return formatted_string


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

	def __init__(self, heading, information):
		super(Synonyms, self).__init__(heading, information)
