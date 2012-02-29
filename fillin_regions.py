f = open('gendagediff_vids_complete1.csv','r')
fnew = open('genagediffcomplete2.csv','w')

regions = ["North America", "Latin/Central/South America","East Asia","Southeast Asia","South Asia","Western Europe", "Mediterranean", "Middle East/North Africa", "Pacific"]

continents = ["North America","South America","Asia","Europe","Africa"]
#considering Australia part of Asia for these purposes

# def writeline(wordlist,termlist,baseline,writefile):
# 	if wordlist[1] in termlist:
# 		s = '%s,%s,%s' % (baseline,)
		
x = f.readlines()
f.close()
# k, the correct output for the first line appears on the last line in the new file, nothing else. hmm 


for line in x:
	splitline = line.split(',')
	line2 = line[:-1]
	if splitline[1] == "Canada" or splitline[1] == "United States":
		fnew.write('%s,%s,%s' % (line2,regions[0],continents[0]))
	#	fnew.write(s)
	elif splitline[1] == "Mexico" or splitline[1] == "Colombia" or splitline[1] == "Brazil":
		fnew.write('%s,%s,%s' % (line2,regions[1],continents[1]))
	#	fnew.write(s)
	elif splitline[1] == "Indonesia" or splitline[1] == "Malaysia" or splitline[1] == "Thailand":
		fnew.write('%s,%s,%s' % (line2,regions[3],continents[2]))
	#	fnew.write(s)
	elif splitline[1] == "India":
		fnew.write('%s,%s,%s' % (line2,regions[4],continents[2]))
	#	fnew.write(s)
	elif splitline[1] == "Japan" or splitline[1] == "China":
		fnew.write('%s,%s,%s' % (line2,regions[2],continents[2]))
	#	fnew.write(s)
	elif splitline[1] == "Germany" or splitline[1] == "United Kingdom" or splitline[1] == "Italy":
		if splitline[1] == "Italy":
			fnew.write('%s,%s,%s' % (line2,regions[6],continents[3]))
		else:
			fnew.write('%s,%s,%s' % (line2,regions[5],continents[3]))
	#	fnew.write(s)
	elif splitline[1] == "Australia":
		# remember here the last region is Pacific, hence -1
		fnew.write('%s,%s,%s' % (line2,regions[-1],continents[2]))
	#	fnew.write(s)
	elif splitline[1] == "Saudi Arabia" or splitline[1] == "Pakistan" or splitline[1] == "Egypt":
		if splitline[1] == "Egypt":
			fnew.write('%s,%s,%s' % (line2,regions[7],continents[-1]))
		else:
			fnew.write('%s,%s,%s' % (line2,regions[7],continents[2]))
	#	fnew.write(s)
	else:
		fnew.write('%s,%s,%s' % (line2, "Unknown", "SHOULD NOT APPEAR"))
	#	fnew.write(s)
fnew.close()

	