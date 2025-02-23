#6
def reverse_words(sentence):
    words = sentence.split()
    reversed = ' '.join(words[::-1])
    return reversed

print(reverse_words("We are ready"))
