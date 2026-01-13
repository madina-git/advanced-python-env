import string

# Открываем файл с явной кодировкой utf-8
with open("C:\\Users\\User\\OneDrive\\Desktop\\advanced-python-env\\text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Count lines
line_count = len(lines)

# Count words
word_count = 0
words_list = []

for line in lines:
    words = line.lower().split()
    word_count += len(words)
    words_list += words

# Count word frequency
word_frequency = {}

for word in words_list:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# Write result to file
with open("analysis.txt", "w", encoding="utf-8") as result:  # тоже с utf-8
    result.write("Lines: " + str(line_count) + "\n")
    result.write("Words: " + str(word_count) + "\n")
    result.write("Word frequency:\n")

    for word in word_frequency:
        result.write(word + " : " + str(word_frequency[word]) + "\n")
