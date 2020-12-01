import csv
import string
import nltk
# punc = "!\"#$%&()*+, -./:;<=>?@[\\]^_{|}~"
punc = string.punctuation

main_dict = {}

def file_count(filename):
	file_dict = {}
	with open(filename) as f:
		data = f.read()
		data = data.lower()
		data = data.replace("'","")
		data = data.replace("`","")
		for s in punc:
			data = data.replace(s," ")
		for n in range(10):
			data = data.replace(str(n),"")

		data = nltk.word_tokenize(data)
		for word in data:
			try:
				file_dict[word]+=1
			except:
				file_dict[word]=1

	return file_dict

N = 16
for file_number in range(1,N+1):
	filename = "documents/d"+str(file_number)+".txt"
	file_dict = file_count(filename)
	for i in file_dict:
		try:
			main_dict[i]+= " "+ str(file_number)+"-"+str(file_dict[i])
		except:
			main_dict[i] = str(file_number)+"-"+str(file_dict[i])
			# main_dict[i].append((file_number,file_dict[i]))

with open("q1.csv","w") as csvfile:
	csvwriter = csv.writer(csvfile)
	csvwriter.writerow(["Word"," DocumentID-Frequency of the word"])
	for i in sorted(main_dict.keys()):
		csvwriter.writerow([i," " + main_dict[i]])