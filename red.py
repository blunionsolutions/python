#!/usr/bin/env python
  
import sys
  
# maps words to their counts
currentKey = None
currentVal = 0
currentCnt = 0

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()   
	# parse the input we got from map.py
	keyval = line.split('|')
	key = keyval[0]  
	val = keyval[1]
	try:
		val = float(val)
	except ValueError:
		val = 0.0
	
	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	if currentKey == key:
		currentVal += val
		currentCnt += 1
	else:
		if currentKey:
			print '%s %f %d' % (currentKey, currentVal/currentCnt, currentCnt)
		currentKey = key
		currentVal = val
		currentCnt = 1
# last group
if currentKey == key:
	print '%s %f %d' % (currentKey, currentVal/currentCnt,currentCnt)
	
