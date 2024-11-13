def word_indices(text):
    words = text.split()  # Split the text into words
    result = {}
    
    for index, word in enumerate(words):
        if word not in result:
            result[word] = []  # Initialize a list for the word
        result[word].append(index)  # Append the index of the word
    
    return result

# Example usage
text = "the quick brown fox jumps over the lazy dog the fox"
print(word_indices(text))
