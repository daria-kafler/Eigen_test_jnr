import string


def find_count_word(filename, data):
  try: 

    file = open(filename, "r")
    read = file.readlines()
    file.close()
    to_string = str(read)
    read_clean = to_string.translate(str.maketrans("", "", string.punctuation))
    read_lowercase = read_clean.lower()
    read_list = list(read_lowercase.split(" "))
    for word in data:
      searched_word = word.lower()
      count = 0
      for sentence in read_list:
        line = sentence.split()
        string_text = str(line)
    if searched_word == line:
        print("searched word:", searched_word, "string in text:", string_text)
        count += 1
    # print(searched_word, ":", count)
    elif searched_word != string_text:
      print("words don't match!")
      
  except FileExistsError:
    print("where file?")

find_count_word("doc1.txt", ["for"])


  