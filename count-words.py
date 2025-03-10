import re
from collections import Counter
top_n = 10  # number of top used words
min_letters = 9 # number of minimum letters

def count_words(text):
    # define regex patterns
    countenance_pattern = r'\bcountenance\w*\b'  # also counts words with different endings
    endeavour_pattern = r'\bendeavour\w*\b'
    word_pattern = fr'\b[a-zA-Z]{{{min_letters},}}\b'
    # show top used words with at least min_letters letters to avoid common words like "and"

    # find all occurrences of the patterns, ignore case
    countenance_matches = re.findall(countenance_pattern, text, re.IGNORECASE)
    endeavour_matches = re.findall(endeavour_pattern, text, re.IGNORECASE)
    all_matches = re.findall(word_pattern, text, re.IGNORECASE)

    return countenance_matches, endeavour_matches, all_matches

# import the text of the Frankenstein book
def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text
text = read_file('Frankenstein.txt')

# use the function count_words on the text
countenance_matches, endeavour_matches, all_matches = count_words(text)

# list unique entries of the matches
unique_countenance_matches = list(set(countenance_matches))
unique_endeavour_matches = list(set(endeavour_matches))

# get the top_n words
def find_top_words(all_matches, top_n=top_n):
    # use Counter to count occurrences of each word
    word_counts = Counter(all_matches)
    # get the most common words
    most_common = word_counts.most_common(top_n)
    # create a list of tuples (word, count)
    return most_common

top_words = find_top_words(all_matches, top_n=top_n)
print(f"\nThe {top_n} most common words with at least {min_letters} letters:")
for word, count in top_words:
    print(f"{word}: {count}")


print(f"{unique_countenance_matches}: {len(countenance_matches)}")
print(f"{unique_endeavour_matches}: {len(endeavour_matches)}")

# print(all_matches)  # to check what the regex is counting