#!/usr/bin/env python


import urllib2

data = urllib2.urlopen("https://en.wiktionary.org/w/index.php?action=raw&title=example")
source = data.read()

print source
