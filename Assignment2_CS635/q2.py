import csv
import string
# punc = "!\"#$%&()*+,-./:;<=>?@[\\]^_{|}~"
punc = string.punctuation

main_dict = {}
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
stopwords = stopwords.words("english")

new_stop_words=[word for word in stopwords]
for word in stopwords:
	cleaned=word.replace("'","")
	if cleaned not in new_stop_words:
		new_stop_words.append(cleaned)
	
stopwords=new_stop_words

ps = PorterStemmer()

def file_count(filename,filenumber):
	with open(filename) as f:
		data = f.read()
		# data = data.lower()
		# data = data.replace("`","")
		data = data.replace("'","")
		for s in punc:
			data = data.replace(s," ")
		for n in range(10):
			data = data.replace(str(n),"")
		data_tokens = word_tokenize(data)
		seen = set()
		for word in data_tokens:
	 		stemmed = ps.stem(word.lower())
	 		if (stemmed not in stopwords) and (stemmed not in seen):
				 try:
					 main_dict[stemmed].append(filenumber)
				 except:
					 main_dict[stemmed] = [filenumber]
				 seen.add(stemmed)

N = 16
for file_number in range(1,N+1):
	filename = "documents/d"+str(file_number)+".txt"
	file_count(filename,file_number)

with open("q2.csv","w") as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(["ID"," Word"," DocID"])
	id = 1
	for i in sorted(main_dict.keys()):
		csvwriter.writerow([id," "+str(i)," " + " ".join([str(x) for x in main_dict[i]])])
		id+=1