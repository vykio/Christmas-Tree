#!/usr/bin/python

n = input('Height (>4): ')
if n < 2:
	print "WTF?! Your tree is too small ! I'll make it higher\n"
	n = 4

i = 1
while i <= n:
	print (n/3)*" " + (n-i)*' ' + (i-1)*'*_' + '*'
	i += 1

print "\nMerry Christmas!"
