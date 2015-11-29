def padla(text):
    word = ""
    for letter in text:
        if letter.istitle():
           x = letter
           word = x + word
    word = word[::-1]
    return word
print(padla("How are you?Eh, ok. Low or Lower?Ohhh."))


