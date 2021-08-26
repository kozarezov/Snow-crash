#!/usr/bin/env python
import sys
arg = sys.argv[1]

s = list(arg)
for i in range (0, len(arg)):
	s[i] = chr(ord(s[i]) - i)
str = ''.join(s)
print(str)