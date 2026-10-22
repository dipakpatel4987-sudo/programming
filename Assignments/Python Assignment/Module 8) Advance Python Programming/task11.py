import re


text = "Python programming is easy to learn."


word = "programming"


result = re.search(word, text)


if result:
    print("Word found in the string.")
    print("Found at position:", result.start())
else:
    print("Word not found.")