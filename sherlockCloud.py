import sys
import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, WhitespaceTokenizer
from nltk.tokenize import sent_tokenize
import re
import string
from nltk.stem import WordNetLemmatizer
from ngram import NGram
from nltk.tag.stanford import NERTagger
from nltk.corpus import wordnet as wn
from enum import Enum

Month = Enum('Month', 'January February March April June July May August September October November Decemeber')

class Month(Enum):
    January 	= 1
    February  	= 2
    March 		= 3
    April 		= 4
    May 		= 5
    June 		= 6
    July  		= 7
    August 		= 8
    September 	= 9
    October 	= 10
    November 	= 11
    Decemeber 	= 12
    
import urllib2
import json

reload(sys)
sys.setdefaultencoding("utf-8")


f = urllib2.urlopen('http://api.wunderground.com/api/4ab5a36ab8ce63df/history_19940625/q/CA/Santa_barbara.json')
json_string = f.read()
parsed_json = json.loads(json_string)
#print parsed_json

result = {}
result['rain'] 					= parsed_json['history']['dailysummary'][0]['rain']
result['snow'] 					= parsed_json['history']['dailysummary'][0]['snow']
result['snowfallm'] 			= parsed_json['history']['dailysummary'][0]['snowfallm']
result['snowfalli']				= parsed_json['history']['dailysummary'][0]['snowfalli']
result['hail'] 					= parsed_json['history']['dailysummary'][0]['hail']
result['thunder'] 				= parsed_json['history']['dailysummary'][0]['thunder']
result['tornado'] 				= parsed_json['history']['dailysummary'][0]['tornado']
result['meantempm'] 			= parsed_json['history']['dailysummary'][0]['meantempm']
result['meantempi'] 			= parsed_json['history']['dailysummary'][0]['meantempi']
result['meandewptm'] 			= parsed_json['history']['dailysummary'][0]['meandewptm']
result['meandewpti'] 			= parsed_json['history']['dailysummary'][0]['meandewpti']
result['meanpressurem'] 		= parsed_json['history']['dailysummary'][0]['meanpressurem']
result['meanpressurei'] 		= parsed_json['history']['dailysummary'][0]['meanpressurei']
result['meanwindspdm'] 			= parsed_json['history']['dailysummary'][0]['meanwindspdm']
result['meanwindspdi'] 			= parsed_json['history']['dailysummary'][0]['meanwindspdi']
result['meanwdire'] 			= parsed_json['history']['dailysummary'][0]['meanwdire']
result['meanwdird'] 			= parsed_json['history']['dailysummary'][0]['meanwdird']
result['meanvism'] 				= parsed_json['history']['dailysummary'][0]['meanvism']
result['meanvisi'] 				= parsed_json['history']['dailysummary'][0]['meanvisi']
result['humidity'] 				= parsed_json['history']['dailysummary'][0]['humidity']
result['maxtempm'] 				= parsed_json['history']['dailysummary'][0]['maxtempm']
result['maxtempi'] 				= parsed_json['history']['dailysummary'][0]['maxtempi']
result['mintempm'] 				= parsed_json['history']['dailysummary'][0]['mintempm']
result['mintempi'] 				= parsed_json['history']['dailysummary'][0]['mintempi']
result['maxhumidity'] 			= parsed_json['history']['dailysummary'][0]['maxhumidity']
result['minhumidity'] 			= parsed_json['history']['dailysummary'][0]['minhumidity']
result['maxdewptm'] 			= parsed_json['history']['dailysummary'][0]['maxdewptm']
result['maxdewpti'] 			= parsed_json['history']['dailysummary'][0]['maxdewpti']
result['mindewptm'] 			= parsed_json['history']['dailysummary'][0]['mindewptm']
result['mindewpti'] 			= parsed_json['history']['dailysummary'][0]['mindewpti']
result['maxpressurem'] 			= parsed_json['history']['dailysummary'][0]['maxpressurem']
result['maxpressurei'] 			= parsed_json['history']['dailysummary'][0]['maxpressurei']
result['minpressurem'] 			= parsed_json['history']['dailysummary'][0]['minpressurem']
result['minpressurei'] 			= parsed_json['history']['dailysummary'][0]['minpressurei']
result['maxwspdm'] 				= parsed_json['history']['dailysummary'][0]['maxwspdm']
result['maxwspdi'] 				= parsed_json['history']['dailysummary'][0]['maxwspdi']
result['minwspdm'] 				= parsed_json['history']['dailysummary'][0]['minwspdm']
result['minwspdi'] 				= parsed_json['history']['dailysummary'][0]['minwspdi']
result['maxvism'] 				= parsed_json['history']['dailysummary'][0]['maxvism']
result['maxvisi'] 				= parsed_json['history']['dailysummary'][0]['maxvisi']
result['minvism'] 				= parsed_json['history']['dailysummary'][0]['minvism']
result['minvisi'] 				= parsed_json['history']['dailysummary'][0]['minvisi']
result['gdegreedays'] 			= parsed_json['history']['dailysummary'][0]['gdegreedays']
result['heatingdegreedays'] 	= parsed_json['history']['dailysummary'][0]['heatingdegreedays']
result['coolingdegreedays'] 	= parsed_json['history']['dailysummary'][0]['coolingdegreedays']
result['precipm'] 				= parsed_json['history']['dailysummary'][0]['precipm']
result['precipi']				= parsed_json['history']['dailysummary'][0]['precipi']
result['default'] 				= 0
print result
print

#print "rain " 			   + rain 			
#print "snow " 			   + snow 			
#print "snowfallm "  	   + snowfallm 		
#print "snowfalli "		   + snowfalli 		
#print "hail "		  	   + hail 			
#print "thunder "		   + thunder 		
#print "tornado "		   + tornado 		
#print "meantempm "		   + meantempm 		
#print "meantempi "		   + meantempi 		
#print "meandewptm "		   + meandewptm 		
#print "meandewpti "		   + meandewpti 		
#print "meanpressurem "	   + meanpressurem 	
#print "meanpressurei "	   + meanpressurei 	
#print "meanwindspdm "	   + meanwindspdm 	
#print "meanwindspdi "	   + meanwindspdi 	
#print "meanwdire "		   + meanwdire 		
#print "meanwdird "		   + meanwdird 		
#print "meanvism "		   + meanvism 		
#print "meanvisi "		   + meanvisi 		
#print "humidity "		   + humidity 		
#print "maxtempm "		   + maxtempm 		
#print "maxtempi "		   + maxtempi 		
#print "mintempm "		   + mintempm 		
#print "mintempi "		   + mintempi 		
#print "maxhumidity "	   + maxhumidity 	
#print "minhumidity "	   + minhumidity 	
#print "maxdewptm "		   + maxdewptm 		
#print "maxdewpti "		   + maxdewpti 		
#print "mindewptm "		   + mindewptm 		
#print "mindewpti "		   + mindewpti 		
#print "maxpressurem "	   + maxpressurem 	
#print "maxpressurei "	   + maxpressurei 	
#print "minpressurem "	   + minpressurem 	
#print "minpressurei "	   + minpressurei 	
#print "maxwspdm "		   + maxwspdm 		
#print "maxwspdi "		   + maxwspdi 		
#print "minwspdm "		   + minwspdm 		
#print "minwspdi "		   + minwspdi 		
#print "maxvism "		   + maxvism 		
#print "maxvisi "		   + maxvisi 		
#print "minvism "		   + minvism 		
#print "minvisi "		   + minvisi 		
#print "gdegreedays "	   + gdegreedays 	
#print "heatingdegreedays " + heatingdegreedays 
#print "coolingdegreedays " + coolingdegreedays 
#print "precipm "		   + precipm 		
#print "precipi "		   + precipi		

def factCheck(parameterMin="default", numberMin=0, parameterMax="default", numberMax=0, parameterMean="default", numberMean=0):
	if (int(result[parameterMin]) <= numberMin and 
		int(result[parameterMax]) >= numberMax and 
		int(result[parameterMean]) is numberMean):
		print "True Fact Check"
	else:
		if(not(result[parameterMin] <= numberMin)):
			print result[parameterMin], " <= "  ,numberMin
		if(not(result[parameterMax] >= numberMax)):
			print result[parameterMax], " >= "  ,numberMax
		if(not(result[parameterMean] is numberMean)):
			print result[parameterMean]," = "   ,numberMean

		print "False Fact Check"

factCheck("mintempi",59, "maxtempi",81, "meantempi",68)
#print 
f.close()

def date_compare(sent1, sent2):
	#include fuzzy with high barrier/ ways to include more words?
	a =  st.tag(('Last friday night we went shopping and then during wednesday ').split())
	b =  st.tag(('Last thursday night we drank to the old year on Wednesday').split())
	print a
	print b
	strip_sent1 = []
	strip_sent2 = []

	for c in a:
		if c[1] != 'O':
			strip_sent1.append(c)
	print strip_sent1		

	for c in b:
		if c[1] != 'O':
			strip_sent2.append(c)
	print strip_sent2
	count = 0.0
	for d in strip_sent1: 
		for e in strip_sent2:
			if d == e:
				print d
				print e
				count += 1
	
	if len(strip_sent1) > len(strip_sent2):
		print count/(len(strip_sent2))
	else:
		print count/(len(strip_sent1))

def _dateExtract(sent):
	a = st.tag((sent).split())
	stripDate = {}
	print a
	print
	for i, item in enumerate(a):
		if(a[i][1] == "DATE" and a[i][0] != ','):
			#if(str(a[i][0]) == "June"):
			#	stripDate[str(a[i][0])] = "dateMonth"
			#elif(str(a[i][0]) == "25th"):
			#	stripDate[str(a[i][0])] = "dateDay"
			#elif(str(a[i][0]) == "1994"):
			#	stripDate[str(a[i][0])] = "dateYear"
			stripDate[str(a[i][0])] = "dateYear"

	print stripDate
	_formDate(stripDate)

def _formDate(date):
	print "poop"
	#http://api.wunderground.com/api/4ab5a36ab8ce63df/history_19940625/q/CA/Santa_barbara.json

#def stream(head, tail, *rest, **kwargs):
#	if kwargs.key("lazy") 
#		# do something here
#
#	if kwargs.key(""):
#
#stream(x, y, lazy = True)
#
#stream(x, y, 0, 0, 0, 0, x= "hello")

st = NERTagger('/Users/dspoka/Desktop/Afact/NLP/stanford-ner/classifiers/english.muc.7class.distsim.crf.ser.gz',
		'/Users/dspoka/Desktop/Afact/NLP/stanford-ner/stanford-ner-3.4.1.jar') 

_dateExtract("I fucked a girl named May who was born on June 25th, 1994")



