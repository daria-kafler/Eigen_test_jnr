from fileinput import filename
import string
import nltk
from nltk.corpus import stopwords
import glob

map = dict()
def word_freq_in_file(filename):
	file = open(filename)
	lines = file.readlines()
	line_positions = 1
	for line in lines:
		clean_line = line.translate(str.maketrans("", "", string.punctuation)).replace("\n"," ").lower()
		word_positions = 1
		words = clean_line.split()
		for word in words:
			# first time we see a word, add to map.
			if word not in map:
				map[word] = dict(count = 0, positions = list())
			# updates counts and word positions
			map[word]["count"] = map[word]["count"] + 1
			map[word]["positions"].append(dict(line = line_positions, word = word_positions, filename = filename))
				
			word_positions += 1
		line_positions += 1
# allows word_freq_in_file function to access all files in specified folder.
all_files = glob.glob("./data/*.txt")
for file in all_files:
	word_freq_in_file(file)

en_stopwords = set(stopwords.words('english'))
# sorts keys by count in descending order
sorted_words = sorted(map.keys(), key = lambda x: map[x]["count"], reverse = True)
for word in sorted_words:
	# removes common stopwords and shows only words that appear over 5 times.
	if word not in en_stopwords and word not in ["went","werent","say","us"] and map[word]["count"] > 5:
		print("Found '{}' {} times".format(word, map[word]["count"]))		
		for position in map[word]["positions"]:
			print("\t Line {}, Word {}, Document '{}'".format(position["line"], position["word"], position["filename"]))

