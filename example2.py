def word_frequency(text: str) -> dict:
    words = text.replace(".", "").replace("!", "").replace(",", "").lower().split()
    frequency = {}
    for word in words:
        if word in words:
            frequency[word] = words.count(word)
    return frequency
print(word_frequency("Hello world! Hello everyone."))
print(word_frequency("This is a test. This test is easy."))
print(word_frequency("Python is fun. Fun fun fun!"))
print(word_frequency("One word , one word."))
