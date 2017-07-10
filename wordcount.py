# put your code here.
def word_count(file_name):
    """"Takes in a file, counts the number of words and prints out 
        each word with the word count"""

    text_file = open(file_name)

    counted_words = {}

    file_words = []

    for line in text_file:
        line = line.rstrip()
        words = line.split(" ")
        for word in words:
            file_words.append(word)

    for each_word in file_words:
        counted_words[each_word] = counted_words.get(each_word, 0) + 1

    for dict_word, dict_word_count in counted_words.iteritems():
        print dict_word, dict_word_count

    text_file.close()

word_count("twain.txt")


