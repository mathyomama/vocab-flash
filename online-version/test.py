#!/usr/bin/env python


import re
import urllib2

#data = urllib2.urlopen("https://en.wiktionary.org/w/index.php?action=raw&title=example")
#
#equal = re.compile(r"=+.*=+")
#
#for line in data:
#	if equal.match(line)==None:
#		continue
#	else:
#		print equal.match(line).group()


class Shape(object):
	def __init__(self, shapename):
		self.shapename = shapename


class ColoredShape(Shape):
	def __init__(self, color, shapename):
		self.color = color
		super(ColoredShape, self).__init__(shapename)
		self.something = self.shapename


cs = ColoredShape('red', 'circle')
print cs.color, cs.shapename, cs.something

cs1 = ColoredShape('red', shapename='circle')
print cs1.color, cs1.shapename

cs2 = ColoredShape(color='red', shapename='circle')
print cs2.color, cs2.shapename

cs3 = ColoredShape(shapename='circle', color='red')
print cs3.color, cs3.shapename



def foo(**kwargs):
	print kwargs


foo(dog='cat', cat='mouse', mouse='cheese')
