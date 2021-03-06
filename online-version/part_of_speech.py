from section import PartOfSpeech


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

