#!/usr/bin/env python


import defi


def main():
	print "What word would you like to define?"
	word = raw_input("> ")
	my_definition = defi.definition(word)
	print my_definition
	if my_definition != None:
		print my_definition.entry.get_headings()

if __name__ == "__main__":
	main()

