import re


text = "Python is a powerful programming language."

word = "Python"

result = re.match(word, text)


if result:
    print("Word matched at the beginning of the string.")
    print("Matched word:", result.group())
else:
    print("Word not matched.")