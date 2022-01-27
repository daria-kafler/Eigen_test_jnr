from fileinput import filename
import string
import nltk
from nltk.corpus import stopwords
import glob

map = dict()
def word_freq_in_file(filename):
	file = open(filename)
	lines = file.readlines()
	line_pos = 1
	for line in lines:
		clean_line = line.translate(str.maketrans("", "", string.punctuation)).replace("\n"," ").lower()
		word_pos = 1
		words = clean_line.split()
		for word in words:
			# first time we see a word, add to map
			if word not in map:
				map[word] = dict(count = 0, positions = list())
				
			# updates counts and positions
			map[word]["count"] = map[word]["count"] + 1
			map[word]["positions"].append(dict(line = line_pos, word = word_pos, filename = filename))
				
			word_pos += 1
		line_pos += 1



all_files = glob.glob("./data/*.txt")
for file in all_files:
	word_freq_in_file(file)

# sorts keys by count in descending order
en_stopwords = set(stopwords.words('english'))
sorted_words = sorted(map.keys(), key = lambda x: map[x]["count"], reverse = True)
for word in sorted_words:
	# removes stopwords
	if word not in en_stopwords and word not in ["went","werent","say", "us"] and map[word]["count"] > 5:
		print("Found '{}' {} times".format(word, map[word]["count"]))		
		for position in map[word]["positions"]:
			print("\t Line {}, Word {}, Document '{}'".format(position["line"], position["word"], position["filename"]))

