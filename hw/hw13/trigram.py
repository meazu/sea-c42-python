
import sys
import random


# Function take sting as input and returns list of words.
def words(string):

    text = string.lower()
    words = text.split()

    # remove the bare single quotes
    words = [word for word in words if word != "'"]
    return words


# Function take filename and returns the  list of lines.
def read_in_data(infilename):

    infile = open(infilename, 'r')
    full_text = []
    aline = infile.readline()
    while aline:
        full_text.append(aline)
        aline = infile.readline()

        # read the rest of the file line by line
    return " ".join(full_text)


# Function generates the trigram
def trigram(words):

    word_pairs = {}
    # loop through the words
    for i in range(len(words) - 2):
        pair = tuple(words[i:i+2])
        nextword = words[i+2]
        word_pairs.setdefault(pair, []).append(nextword)
    return word_pairs


def text(word_pairs, no_of_lines):

    new_text = []
    # Testing for 30 lines
    no_of_lines = 20
    for i in range(no_of_lines):
        # pick a word pair to start the sentence
        sentence = list(random.choice(list(word_pairs.keys())))

        # now add a random number of additional words to the sentence
        for j in range(random.randint(2, 4)):
            pair = tuple(sentence[-2:])
            sentence.append(random.choice(word_pairs[pair]))
        # capitalize the first word:
        sentence[0] = sentence[0].capitalize()

        sentence[-1] += u"."
        new_text.extend(sentence)

    new_text = " ".join(new_text)

    return new_text
if __name__ == "__main__":

    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = read_in_data(filename)
    infile = open(filename, "r")
    linelist = infile.readlines()
    no_of_lines = len(linelist)

    words = words(in_data)
    word_pairs = trigram(words)
    new_text = text(word_pairs, no_of_lines)

    print(new_text)
