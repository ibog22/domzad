def function(text):
    word = ""
    for letter in text:
        if letter.isupper():
           word = word + letter
    return word
print(function("How are you?Eh, ok. Low or Lower?Ohhh."))

