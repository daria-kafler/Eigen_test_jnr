import string



def word_freq_in_file(filename):
	map = dict()
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
				
			# update counts and positions
			map[word]["count"] = map[word]["count"] + 1
			map[word]["positions"].append(dict(line = line_pos, word = word_pos))
				
			word_pos += 1
		line_pos += 1
			
	#sort keys by count in descending order
	sorted_words = sorted(map.keys(), key = lambda x: map[x]["count"], reverse = True)
  #ADD CONDITIONS HERE. remove 'uninteresting words', remove words that appear only once, etc.
	for word in sorted_words:
		print("Found '{}' {} times: ".format(word, map[word]["count"]))		
		for position in map[word]["positions"]:
			print("\t Line {}, Word {}".format(position["line"], position["word"]))
			
			
	
word_freq_in_file("./data/doc1.txt")

