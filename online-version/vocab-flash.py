#!/usr/bin/env python


import defi


def main():
	print "What word would you like to define?"
	word = raw_input("> ")
	print ""
	my_definition = defi.Definition(word)
	my_definition.print_entry()



if __name__ == "__main__":
	main()

