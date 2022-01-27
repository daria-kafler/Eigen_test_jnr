import string
import nltk
from nltk.corpus import stopwords
import glob


def word_freq_in_file(filename):
	map = dict()
	file = open(filename)
	lines = file.readlines()
	line_pos = 1
	en_stopwords = set(stopwords.words('english'))
	for line in lines:
		clean_line = line.translate(str.maketrans("", "", string.punctuation)).replace("\n"," ").lower()
		word_pos = 1
		words = clean_line.split()
		for word in words:
			# first time we see a word, add to map
			if word not in map:
				map[word] = dict(count = 0, positions = list())
				
			# update counts and positions
			map[word]["count"] = map[word]["count"] + 1
			map[word]["positions"].append(dict(line = line_pos, word = word_pos))
				
			word_pos += 1
		line_pos += 1
			
	#sort keys by count in descending order
	sorted_words = sorted(map.keys(), key = lambda x: map[x]["count"], reverse = True)
	for word in sorted_words:
  	#removes stopwords
		if word not in en_stopwords and word not in ["went","werent","say"] and map[word]["count"] > 10:
			print("Found '{}' {} times: ".format(word, map[word]["count"]))		
			for position in map[word]["positions"]:
				print("\t Line {}, Word {}, In Document {}".format(position["line"], position["word"],filename))


all_files = glob.glob("./data/*.txt")
for file in all_files:
	print("THIS IS A NEW FILE {}".format(file))
	word_freq_in_file(file)


