import fileinput

video01 = "9u9A2mktG7s" 
video02 = "70TPrfL_8-M"
video03 = "D1MMlaDm5t0"
video04 = "DrAGfaLlTlk"
video05 = "HlsjRsemzLI"
video06 = "kvQWKcMdyS4"
video07 = "RncWwulYGTA"
video08 = "RRbuz3VQ100"
video09 = "vmlLj1aLZ7s"

#base_fname = "2012_02_11 - AHON-YouTube-%s-Demographics.csv"



# takes a unique string to plug into base .csv filename
def age_video_percents(vidfname):
	base_fname = "2012_02_11 - AHON-YouTube-%s-Demographics.csv"
	#gender_country = {}
	age_country = {}
#	infodict_list = []
	fn = base_fname % (vidfname)
	f = open(fn, 'r')
	fr = f.read().split('\r')

	for line in fr:
	#	print line # this is for debugging, but it's not printing anything. why do I do this
		linvals = line.split(',')
	#	print linvals # this doesn't seem to be printing anything either
		# filling gender_country
	
		# filling age_country
	#	if type(linvals[1]) == string:
			# don't do anything... this conditional should be different
		if int(linvals[1].split('-')[0]) < 35 and linvals[0] in age_country:
			age_country[linvals[0]] += float(linvals[3])
		elif int(linvals[1].split('-')[0]) < 35 and linvals[0] not in age_country:
			age_country[linvals[0]] = float(linvals[3])	
	#infodict_list.append(gender_country)
	#infodict_list.append(age_country)
	return age_country
	
def gend_vid_percents(vidfname):
	base_fname = "2012_02_11 - AHON-YouTube-%s-Demographics.csv"
	gender_country = {}	
	fn = base_fname % (vidfname)
	f = open(fn, 'r')
	fr = f.read().split('\r')

	for line in fr:
		linvals = line.split(',')
		
		if linvals[2] == 'f' and linvals[0] in gender_country:
			gender_country[linvals[0]] += float(linvals[3])
		elif linvals[2] == 'f' and linvals[0] not in gender_country:
			gender_country[linvals[0]] = float(linvals[3])
	return gender_country
	
# takes a list of dictionaries, prints
def printvidpercents(ldict):
	for w in sorted(ldict,key=ldict.get, reverse=True):
		print w, "%0.1f" % ldict[w]	


# further generalizing fxns!
videolist = [video01, video02, video03, video04, video05, video06, video07, video08, video09]

def seelistvidstats(list_of_vids):
	vidgendage = {}
	for item in list_of_vids:
		x = age_video_percents(item)
		y = gend_vid_percents(item)
		print "\nPercent of young viewers for Video Key--%s" % item
		printvidpercents(x)
		print "\nPercent of female viewers for Video Key--%s" % item
		printvidpercents(y)
		vidgendage[item] = vidgendage.get(item,(x,y))
		return vidgendage

newdict = seelistvidstats(videolist)
print
print newdict
		
		





# CODE TIME

#seelistvidstats(videolist)

# x = age_video_percents(video01) # there's nothing in the dictionaries. yay. ...
# y = gend_vid_percents(video01)
# #print x
# #print y
# printvidpercents(x)
# print
# printvidpercents(y)
#	print "hi"
#print printvidpercents(x) # returns None when the fxn returns something..