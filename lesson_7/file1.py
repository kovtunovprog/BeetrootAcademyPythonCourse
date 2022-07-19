import string

a_string = input('Your string...:\n')
translator = str.maketrans('', '', string.punctuation)
a_string = a_string.translate(translator)
list_of_word = a_string.split(' ')
unique_words = {}
for word in list_of_word:
    if word in unique_words:
        continue
    unique_words[word] = list_of_word.count(word)
print(unique_words)
