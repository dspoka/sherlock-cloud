import csv
from nltk.corpus import wordnet as wn
import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, WhitespaceTokenizer
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer

#0 id
#1 Tweet
#2 state
#3 location
#4 s1,"I can't tell"
#5 s2,"Negative"
#6 s3,"Neutral / author is just sharing information"
#7 s4,"Positive"
#8 s5,"Tweet not related to weather condition"  
#9 w1,"current (same day) weather"
#10 w2,"future (forecast)"
#11 w3,"I can't tell"
#12 w4,"past weather"
#13 k1,"clouds"
#14 k2,"cold"
#15 k3,"dry"
#16 k4,"hot"
#17 k5,"humid"
#18 k6,"hurricane"
#19 k7,"I can't tell"
#20 k8,"ice"
#21 k9,"other"
#22 k10,"rain"
#23 k11,"snow"
#24 k12,"storms"
#25 k13,"sun"
#26 k14,"tornado"
#27 k15,"wind"
# 
def run(data):
	raw_train_data = open(data, 'r')
	train_data = csv.reader(raw_train_data, delimiter = ",")
	emptyList = []
	synHurricane = _getSynonyms("wind")
	for row in train_data:
		tweetWords = row[1].split(" ")		
		for word in tweetWords:
			if(word.lower() in synHurricane):
				print row
def _isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def _wordStem(word):
	return wnl.lemmatize(word)
def _wordTokenizer(Sent_Tokens):
	return WhitespaceTokenizer().tokenize(Sent_Tokens)
def _getSynonyms(word):
	words = []
	for sense in wn.synsets(word):
		for singleWord in sense._lemma_names:
			words.append(str(singleWord))
	words = [oneWord for oneWord in set(words)]
	return words

stopwords = nltk.corpus.stopwords.words('english')
wnl = WordNetLemmatizer()
run('train.csv')
#print _wordStem("hurricane")