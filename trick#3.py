# Using a context manager to do some stuffs for us like closing the file automatically, b4 this we used to close the file manually which sucks sometimes



with open('text.txt', 'r') as f:
    file_contents = f.read()

# f = open('text.txt', 'r')

file_contents = f.read()

# f.close()

words = file_contents.split(' ')
word_count = len(words)
print(word_count)