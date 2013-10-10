#!/usr/bin/env python


import re
import urllib2

data = urllib2.urlopen("https://en.wiktionary.org/w/index.php?action=raw&title=example")

equal = re.compile(r"=+.*=+")

for line in data:
	if equal.match(line)==None:
		continue
	else:
		print equal.match(line).group()
