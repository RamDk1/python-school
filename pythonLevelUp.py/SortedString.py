def sort_words(words):
    return ' '.join(sorted(words.split(), key=str.lower))

print(sort_words("banana,  Apple cherry! date"))